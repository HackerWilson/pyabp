#!/usr/bin/env python
# encoding: utf-8

from __future__ import unicode_literals
import io
import os
import sys
import inspect
import argparse
import pydoc
import pkgutil
from collections import OrderedDict


API_BLUEPRINT_VERSION = '1A'
metadata_format = 'FORMAT: %s' % API_BLUEPRINT_VERSION + os.linesep
metadata_host = ''


class TextDoc(object):

    def analyze_module(self, obj):
        try:
            _all = obj.__all__
        except AttributeError:
            _all = None

        classes = []
        for key, value in inspect.getmembers(obj, inspect.isclass):
            if (_all is not None or (inspect.getmodule(value) or obj) is obj):
                if pydoc.visiblename(key, _all, obj):
                    classes.append(value)

        funcs = []
        for key, value in inspect.getmembers(obj, inspect.isroutine):
            if (_all is not None or inspect.isbuiltin(value) or
                    inspect.getmodule(value) is obj):
                if pydoc.visiblename(key, _all, obj):
                    funcs.append(value)
        return classes, funcs

    def doc_group(self, group, classes, funcs):
        result = ''
        desc = inspect.getdoc(group)
        if desc and desc.startswith('Group'):
            for line in desc.splitlines()[1:]:
                result = os.linesep.join([result, line])

        obj_list = classes + funcs
        for k, v in group_obj(obj_list).items():
            group_head_doc = ''
            group_doc = ''
            for obj in v:
                doc = inspect.getdoc(obj) or ''
                if doc and doc.startswith('Group'):
                    full_doc = doc.splitlines()
                    group_head_doc = get_group_head(full_doc[0])
                    group_head_doc = ' '.join(['#', group_head_doc])
                    for line in full_doc[1:]:
                        group_doc = os.linesep.join([group_doc, line])
                else:
                    group_doc = doc
                group_doc += os.linesep

            doc = os.linesep.join([group_head_doc, group_doc])
            result = os.linesep.join([result, doc])
        return result


text = TextDoc()


def writedoc(module_list):
    all_classes = []
    all_funcs = []
    if isinstance(module_list, list):
        for module in module_list:
            module_classes, module_funcs = text.analyze_module(module)
            all_classes.extend(module_classes)
            all_funcs.extend(module_funcs)
        contents = text.doc_group(module_list[0], all_classes, all_funcs)
        name = module_list[0].__name__

    if contents.strip():
        file = io.open(name + '.md', 'w', encoding='utf8')
        file.write(metadata_format)
        file.write(metadata_host)
        file.write(contents)
        file.close()


def group_obj(obj_list):
    obj_dict = {}
    for idx, obj in enumerate(obj_list):
        obj_doc = inspect.getdoc(obj)

        if obj_doc and obj_doc.startswith('Group'):
            group_head_doc = obj_doc.splitlines()[0]
            obj_dict[obj] = group_head_doc
        else:
            # 非group排序时先处理
            obj_dict[obj] = ''.join([str(idx), obj.__name__])

    obj_list_dict = {}
    order_obj_dict = OrderedDict(sorted(obj_dict.items(), key=lambda t: t[1]))
    for k, v in order_obj_dict.items():
        v = get_group_head(v)
        obj_list_dict.setdefault(v, []).append(k)
    return obj_list_dict


def get_group_head(doc):
    if doc.startswith('Group'):
        for d in doc.split():
            if d.isdigit():
                doc = doc.replace(str(d), '')
    return doc


def resolve(obj):
    try:
        module, name = pydoc.resolve(obj)
        return module, name
    except (ImportError, pydoc.ErrorDuringImport):
        raise


def writedocs(dir_path):
    all_modules = []
    for module_loader, module_name, ispkg in pkgutil.walk_packages([dir_path]):
        module, name = resolve(module_name)
        all_modules.append(module)

    for k, v in group_obj(all_modules).items():
        writedoc(v)


def cli():
    if '' not in sys.path:
        script_dir = os.path.dirname(sys.argv[0])
        if script_dir in sys.path:
            sys.path.remove(script_dir)
        sys.path.insert(0, '.')

    parser = argparse.ArgumentParser(
        description='API Blueprint from python docstring.')

    parser.add_argument('-w', '--write', dest='name', nargs='*',
                        help='''Write out the API Blueprint documentation
                        for a module to a file in the current directory.
                        If <name> contains a '{sep}',
                        it is treated as a filename;
                        if it names a directory,
                        documentation is written for all the contents.''')
    parser.add_argument('--host', dest='host',
                        help='Your host server address.')

    args = parser.parse_args()
    if args.host:
        global metadata_host
        metadata_host = 'HOST: %s' % args.host + os.linesep
    for arg in args.name:
        if pydoc.ispath(arg) and not os.path.exists(arg):
            print('path %r does not exist.' % arg)
            break
        if pydoc.ispath(arg):
            if os.path.isfile(arg):
                obj = pydoc.importfile(arg)
                module, name = resolve(obj)
                module_list = [module]
                writedoc(module_list)
            else:
                sys.path.insert(0, arg)
                writedocs(arg)
        else:
            module, name = resolve(arg)
            module_list = [module]
            writedoc(module_list)


if __name__ == '__main__':
    cli()

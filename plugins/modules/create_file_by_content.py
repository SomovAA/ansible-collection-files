#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: create_file_by_content
short_description: Create file by content to remote location
version_added: "1.0.0"
description: Create file by content to remote location
options:
    path:
        description:
            - The remote absolute path where the file should be created.
        required: true
        type: path
    content:
        description:
            - Sets the contents of a file directly to the specified value.
            - Works only when C(path) is a file. Creates the file if it does not exist.
        required: true
        type: str
author:
    - Somov Aleksey (https://github.com/SomovAA)
'''

EXAMPLES = r'''
# success the module
- name: Test with a message
  somovaa.files.create_file_by_content:
    path: /tmp/1.txt
    content: hello world
'''

RETURN = r'''
changed:
    description:
    type: str
    returned: always
    sample: true
'''

from ansible.module_utils.basic import AnsibleModule

def run_module():
    module_args = dict(
        path=dict(type='path', required=True),
        content=dict(type='str', required=True)
    )

    result = dict(
        changed=False
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if module.check_mode:
        module.exit_json(**result)

    md5_old = module.md5(module.params['path'])

    f = open(module.params['path'], 'w')
    f.write(module.params['content'])
    f.close()

    md5_new = module.md5(module.params['path'])

    if md5_old != md5_new:
        result['changed'] = True

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
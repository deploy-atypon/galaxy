#!/usr/bin/python

DOCUMENTATION = '''
---
module: Calculate g1 heap region size
short_description: Calculate g1 heap region size
description:
    - Need to calculate the 'i' which dividing the heap in mb is closer to 2048 
    
options:
    heap_in_gb:
        required: True
        description:   
            - Solr heap size in GB
'''

EXAMPLES = '''
  - name: find_g1_heap_region_size
    find_g1_heap_region_size:
      heap_in_gb: 8
'''

from ansible.module_utils.basic import AnsibleModule
from requests import Session, exceptions

def main():
    module = AnsibleModule(
        argument_spec = dict(
            heap_in_gb = dict(required=True, type='int')
        )
    )

    heap = module.params['heap_in_gb'] * 1024

    i = 1

    min_regions_diff = abs(2048 - (heap/i))
    while True:
        next_region_diff = abs(2048 - (heap/(i*2)))
        if next_region_diff >= min_regions_diff:
            break
        min_regions_diff = next_region_diff
        i = i*2

    module.exit_json(changed=True, g1_heap_region_size=i)


if __name__ == '__main__':
    main()

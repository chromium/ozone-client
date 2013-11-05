{
  'variables':  {
    'ozone_platform_rdp%': 1,
  },
  'conditions': [
    ['<(ozone_platform_rdp) == 1', {
      'variables':  {
        'external_ozone_platform_deps': [
          '<(DEPTH)/ozone-rdp/rdp.gyp:rdp',
        ],
        'external_ozone_platforms': [
          'rdp'
        ],
        'ozone_platform%': 'rdp',
      },
    }],
  ],
}


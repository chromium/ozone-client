{
  'variables':  {
    'ozone_platform_rfb%': 1,
  },
  'conditions': [
    ['<(ozone_platform_rfb) == 1', {
      'variables':  {
        'external_ozone_platform_deps': [
          '<(DEPTH)/ozone-rfb/rfb.gyp:rfb',
        ],
        'external_ozone_platforms': [
          'rfb'
        ],
        'ozone_platform%': 'rfb',
      },
    }],
  ],
}


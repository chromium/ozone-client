{
  'targets': [
    {
      'target_name': 'rfb',
      'type': 'static_library',
      'dependencies': [
        '<(DEPTH)/base/base.gyp:base',
        '<(DEPTH)/ui/gfx/gfx.gyp:gfx',
        '<(DEPTH)/ui/events/events.gyp:events',
        # additional dependencies for your platform
      ],
      'include_dirs': [
        '..',
      ],
      'sources': [
        # additional source files for your platform
        'ozone_platform_rfb.cc',
        'ozone_platform_rfb.h',
      ],
    },
  ]
}

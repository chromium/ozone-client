{
  'targets': [
    {
      'target_name': 'rdp',
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
        'ozone_platform_rdp.cc',
        'ozone_platform_rdp.h',
      ],
    },
  ]
}

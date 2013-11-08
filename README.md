The purpose of the  [`ozone` platform
abstraction](http://www.chromium.org/developers/design-documents/ozone) is
to permit porting Chromium to a new window system or hardware
platform while keeping most of the port code outside of the Chromium tree.

This project is a sample ozone platform implementation that makes
Chromium into a RFB server and a demonstration of how to setup a
project that augments Chromium.

Getting Started
====

*  Make a directory of your choice. I set a shell variable for this directory to `_o` and the
examples below assume that `_o` has been set.

*  Install the chromium project's depot tools as described in [Install depot_tools](http://dev.chromium.org/developers/how-tos/install-depot-tools) and add this to the path.

*  Set `GYP_DEFINES`:  Something like this maybe.

		GYP_DEFINES='clang=1 component=shared_library use_ash=0 use_aura=1 chromeos=1 use_ozone=1' 

*  Create `$_o/.gclient` containing the following:

		solutions = [
		  {
		    u'managed': True,
		    u'name': u'src',
		    u'url': u'https://chromium.googlesource.com/chromium/src.git', 
		    u'custom_deps': {},
		    u'deps_file': u'.DEPS.git',
		    u'safesync_url': u'',
		    u'custom_vars': {
		      u'webkit_rev': u''
		    }
		  },
		  {
		    "name"  : "src/ozonerfb",
		    "url"  : "https://github.com/chromium/ozone-client.git",
		   },
		  {
		    "name" :  "src/third_party/libvncserver",
		    "url" : "git://git.code.sf.net/p/libvncserver/code",
		   },
		]


*  Run `gclient sync`. Add a `-j`*n* to make it go faster if you have enough
CPU and internet bandwidth.

And presto: Chromium source tree with side-loaded additional source to support
a new platform.

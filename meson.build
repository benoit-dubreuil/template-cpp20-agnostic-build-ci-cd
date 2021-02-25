project('template-repo-cpp-ecosystem', 'cpp',
  version : '0.1',
  default_options : ['c_std=c17',
                     'cpp_std=c++17',
                     'warning_level=3',
                     'b_ndebug=if-release'])

src_dir = 'src/'

exe = executable('template_repo_cpp_ecosystem', src_dir + 'Main.cpp',
  install : true)

test('basic', exe)
 
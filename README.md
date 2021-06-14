# Template Repository : C++ Ecosystem

ABANDONED

LEARNT LESSON : MESON AS A BUILD SYSTEM DOES NOT FIT C++ ECOSYSTEM

Template repository for projects using C++ and its ecosystem.

## Specifications

- **Language** : C++
    - **Version** : 20
    - Agnostic
    - Standard / pedantic
- **OS** : Agnostic (cross-platform)
    - **Officially supports** :
        - *Windows 10*
            - MSVC 1928
            - Clang 12
            - GCC 11
        - *Ubuntu 20.X LTS*
            - Clang 12
            - GCC 11
- **Architecture** : 64-bit
- **Build system generator** : [Meson](https://mesonbuild.com)
- **Package Manager** : [Conan](https://conan.io/)
- **Logging** : [spdlog](https://github.com/gabime/spdlog)
- **Documentation** : [Doxygen](https://www.doxygen.nl)
- **Test** : [Catch2](https://github.com/catchorg/Catch2)
- **CI/CD** : [GitHub Actions](https://github.com/features/actions)
- **VCS** : [Git](https://git-scm.com/)
    - **Host** : [GitHub](https://github.com/), cloud hosted
    - **Workflow** : [GitFlow](https://github.com/nvie/gitflow)
- **Projet management** : [ZenHub](https://www.zenhub.com)
- **Computer Graphics & Visualization API** : [OpenGL](https://www.khronos.org/opengl/)
    - **Version** : 4.6
    - **Implementation** : [GLAD](https://github.com/Dav1dde/glad)
    - **Window & Context** : [GLFW](https://www.glfw.org/)
    - **Mathematics** : [GLM](https://github.com/g-truc/glm)

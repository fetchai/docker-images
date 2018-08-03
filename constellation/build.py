#!/usr/bin/env python3
import os
import shutil
import subprocess


def detect_project_path():
    project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

    print(project_path)

    tests = [
        os.path.isdir(project_path),
        os.path.isdir(os.path.join(project_path, 'docker-images')),
        os.path.isdir(os.path.join(project_path, 'docker-images', 'fetch-ledger-alpine-dev')),
        os.path.isfile(os.path.join(project_path, 'CMakeLists.txt')),
        os.path.isfile(os.path.join(project_path, 'Jenkinsfile')),
        os.path.isfile(os.path.join(project_path, 'LICENSE')),
        os.path.isfile(os.path.join(project_path, 'README.md')),
    ]

    if not all(tests):
        raise RuntimeError('Failed to detect project layout')

    return project_path


def build_alpine_constellation(project_path):
    docker_path = os.path.join(project_path, 'docker-images', 'fetch-ledger-alpine-dev')
    build_image_script_path = os.path.join(docker_path, 'scripts', 'docker-build-img.sh')
    compile_script_path = os.path.join(docker_path, 'scripts', 'docker-make.sh')

    # build the image
    subprocess.check_call([build_image_script_path], cwd=project_path)

    # compile the code (inside the development image)
    subprocess.check_call([compile_script_path], cwd=project_path)


def main():
    working_path = os.path.dirname(__file__)

    # build the parent project first
    project_path = detect_project_path()

    # compile the project
    build_alpine_constellation(project_path)

    # detect the build folder
    build_root = os.path.abspath(os.path.join(project_path, 'build-alpine'))
    if not os.path.isdir(build_root):
        raise RuntimeError('Unable to find build root at: {}'.format(build_root))

    # copy the output folder
    constellation_app_path = os.path.join(build_root, 'apps', 'constellation', 'constellation')
    shutil.copy(constellation_app_path, working_path)

    # build the docker image
    cmd = [
        'docker',
        'build',
        '-t', 'constellation',
        '.'
    ]
    subprocess.check_call(cmd, cwd=working_path)



if __name__ == '__main__':
    main()

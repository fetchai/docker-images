#!/usr/bin/env python3
import os
import shutil
import subprocess
import argparse

GCR_PROJECT = 'organic-storm-201412'


def parse_commandline():
    parser = argparse.ArgumentParser()
    parser.add_argument('--rebuild', action='store_true', help='Rebuild the image')
    parser.add_argument('-p', '--publish', action='store_true', help='Publish the image to GCR')
    return parser.parse_args()


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


def get_project_version(project_root):
    return subprocess.check_output(['git', 'describe', '--dirty'], cwd=project_root).decode().strip()


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

    args = parse_commandline()

    # build the parent project first
    project_path = detect_project_path()
    version = get_project_version(project_path)
    build_root = os.path.abspath(os.path.join(project_path, 'build-alpine'))

    local_docker_tag = 'constellation:{}'.format(version)
    remote_docker_tag = 'gcr.io/{}/{}'.format(GCR_PROJECT, local_docker_tag)

    # clean up
    if args.rebuild:
        shutil.rmtree(build_root)
        os.makedirs(build_root, exist_ok=True)

    # compile the project
    build_alpine_constellation(project_path)

    # detect the build folder
    if not os.path.isdir(build_root):
        raise RuntimeError('Unable to find build root at: {}'.format(build_root))

    # copy the output folder
    constellation_app_path = os.path.join(build_root, 'apps', 'constellation', 'constellation')
    shutil.copy(constellation_app_path, working_path)

    # build the docker image
    cmd = [
        'docker',
        'build',
        '-t', local_docker_tag,
        '.'
    ]
    subprocess.check_call(cmd, cwd=working_path)

    if args.publish:

        # make the remote tag
        cmd = [
            'docker',
            'tag',
            local_docker_tag,
            remote_docker_tag,
        ]
        subprocess.check_call(cmd)

        # push the remote tag
        cmd = [
            'docker',
            'push',
            remote_docker_tag
        ]
        subprocess.check_call(cmd)



if __name__ == '__main__':
    main()

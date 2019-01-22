#!/usr/bin/env python3
import os
import sys
import shutil
import subprocess
import argparse

GCR_PROJECT = 'organic-storm-201412'

PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
CONSTELLATION_PATH = os.path.abspath(os.path.dirname(__file__))


def parse_commandline():
    parser = argparse.ArgumentParser()
    parser.add_argument('--rebuild', action='store_true', help='Rebuild the image')
    parser.add_argument('-p', '--publish', action='store_true', help='Publish the image to GCR')
    parser.add_argument('-f', '--force', dest='normal', action='store_false', help=argparse.SUPPRESS)
    return parser.parse_args()


def check_project_path():
    tests = [
        os.path.isdir(PROJECT_PATH),
        os.path.isdir(os.path.join(PROJECT_PATH, 'docker-images')),
        os.path.isfile(os.path.join(PROJECT_PATH, 'CMakeLists.txt')),
        os.path.isfile(os.path.join(PROJECT_PATH, 'Jenkinsfile')),
        os.path.isfile(os.path.join(PROJECT_PATH, 'LICENSE')),
        os.path.isfile(os.path.join(PROJECT_PATH, 'README.md')),
    ]

    if not all(tests):
        raise RuntimeError('Failed to detect project layout')


def get_project_version():
    return subprocess.check_output(['git', 'describe', '--dirty=-wip'], cwd=PROJECT_PATH).decode().strip()


def main():
    args = parse_commandline()

    # auto detect the projec path
    check_project_path()

    version = get_project_version()

    if args.normal and version.endswith('-wip'):
        print('Unable to publish versions of uncom')
        sys.exit(1)

    # based on the version generate the required tags
    latest_docker_tag = 'constellation:latest'
    local_docker_tag = 'constellation:{}'.format(version)
    remote_docker_tag = 'gcr.io/{}/{}'.format(GCR_PROJECT, local_docker_tag)

    print('Generating source archive...')
    cmd = [
        'git-archive-all', os.path.join(CONSTELLATION_PATH, 'project.tar.gz')
    ]
    subprocess.check_call(cmd, cwd=PROJECT_PATH)
    print('Generating source archive...complete')

    print('Building constellation image...')
    cmd = [
        'docker',
        'build',
        '-t', latest_docker_tag,
        '.',
    ]
    subprocess.check_call(cmd, cwd=CONSTELLATION_PATH)


    # also do the tag the image
    cmd = [
        'docker',
        'tag',
        latest_docker_tag,
        local_docker_tag,
    ]
    subprocess.check_call(cmd)
    print('Building constellation image...complete')

    if args.publish:

        print('Publishing docker image...')

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

        print('Publishing docker image...complete')


if __name__ == '__main__':
    main()

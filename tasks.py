#!/usr/bin/env python
# -*- coding: utf-8 -*-

from invoke import task, run

@task
def test():
    run("python run_tests.py", pty=True)

@task
def clean():
    run("rm -rf build")
    run("rm -rf dist")
    run("rm -rf textblob_fr.egg-info")
    clean_docs()
    print("Cleaned up.")

@task
def publish(test=False):
    """Publish to the cheeseshop."""
    try:
        __import__('wheel')
    except ImportError:
        print("wheel required. Run `pip install wheel`.")
        sys.exit(1)
    if test:
        run('python setup.py register -r test sdist bdist_wheel upload -r test')
    else:
        run("python setup.py register sdist bdist_wheel upload")

@task
def readme():
    run("rst2html.py README.rst > README.html", pty=True)
    run("open README.html")

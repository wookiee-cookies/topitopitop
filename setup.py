from setuptools import find_packages, setup

# ------------------------------------------------------------------------------

if __name__ == "__main__":

    setup(
        name="topitopitop",
        version="v1.0.2",
        description="demo",
        long_description="# foo bar",
        long_description_content_type="text/markdown",
        keywords=["pipy testsing"],
        author="waroo",
        author_email="ihateyoujabba@gmail.com",
        project_urls={
            "GitHub: repo": "https://github.com/wookiee-cookies/topitopitop",
            "Bugtracker": "https://github.com/wookiee-cookies/topitopitop/issues",
        },
        packages=find_packages(exclude=["tests*"]),
        install_requires=[],
        entry_points='''
            [console_scripts]
            deadlinks=deadlinks.__main__:main
        ''',
        zip_safe=False,
        python_requires='>=3.6',
        url="https://github.com/wookiee-cookies/",
        license="",
        platforms=['MacOS', 'Posix', 'Unix'],
        classifiers=[
        ],
    )

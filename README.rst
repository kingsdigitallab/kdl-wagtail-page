KDL Wagtail Page
================

Very basic but reusable Wagtail page models for KDL projects.

Install it with pip or pipenv using the following package name:

kdl-wagtail-page

Requirements: wagtail 2+, django 2+, python 3.5+

The idea is to have a single code base for our Wagtail components.

=> we can just install and use, no coding necessary for simple use cases

=> we don't have to maintain and upgrade a lot of small variants of the same
code which was copied and adapted for each project

For contributors:

* runs out of the box with minimal settings
* keep it generic and relatively simple (code and interface)
* if you need something more advanced (but reusable), create a new page type
* if you need something very specific: subclass into your own project
* keep it focused, it is a package about pages (not menus, search or blogs)
* keep it backward-compatible
* automate the upgrades
* keep it compatible with wagtail and Django 2
* keep it compatible with barebones base.html template blocks


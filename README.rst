Experimental Sphinx-based Fortran Webpage
=========================================

This branch explores the possibility to build the Fortran webpage with sphinx rather than with jekyll.


Building the webpage locally
----------------------------

This webpage is build with sphinx to install the dependencies the conda environment manager is recommended:

.. code::

   conda env create -n sphinx -f conda-env.yaml
   conda activate sphinx

Alternatively, you can use pip and install the dependencies with

.. code::

   pip install -r requirements.txt

Now you should be able to build the webpage with

.. code::

   make html

You can inspect the result under ``_build/html/index.html``.

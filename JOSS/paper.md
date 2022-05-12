---
title: 'An Open-Source modeling of seismic waves scattered by near-surface heterogeneities.'
tags:
  - Python
  - Geophysics
  - Finite difference method
  - Numerical modeling
  - Near surface
  - Scattering
  - Heterogeneities
authors:
  - name: Holger Quintero Santander^[Co-first author] 
    orcid: 0000-0003-3539-3476
    affiliation: 1
  - name: William Mauricio Agudelo Zambrano
    orcid: 0000-0003-4086-878X
    affiliation: 2
  - name: Ivan Javier Sánchez Galvis
    orcid: 0000-0001-9972-9827
    affiliation: 1
affiliations:
 - name: Industrial University of Santander, Colombia
   index: 1
 - name: ECOPETROL S.A. Innovation and Technology Center ICP, Colombia
   index: 2
date: 12 May 2022
bibliography: paper.bib

---

# Summary

Near-surface heterogeneities affect seismic waves causing the wavefield to be scattered, this is evidenced in the seismic records and adds complexity in the signals because the reflections of the body waves are masked with a noise that can become up to 10 times greater than common seismic noise [@Stork:2015], making the task of attenuating it difficult. The modeling of surface waves in the presence of heterogeneities is essential to study the propagation of seismic waves in geophysics and engineering. Using the improved vacuum formulation for 2D finite-difference [@Zeng:2012] who incorporates surface topography to the wave propagation simulation (satisfying the free surface condition) it is possible to observe the scattered wavefield for different earth models with shallow random scattering bodies and irregular topography. In addition, this formulation manages to reduce the computational cost of numerical modeling since it requires fewer grid points per wavelength PPW than other methods and is easy to implement to the conventional vacuum formulation 2D finite-difference. 

The analysis of the results of seismic wave propagation over heterogeneous media helps to understand the scattering mechanisms and, therefore, could lead to the development of new data acquisition and processing techniques to reduce the scattering noise, improve the quality of seismic images and classify scattering. Numerical modeling is presented as an open-source software developed in Python.

# Statement of need

Descripcion del codigo(librerias y funciones tambien)

Paso a paso (parametros, cpml, promediado de parametros, campos y condiciones)


# Examples

Generacion e datos sinteticos y ejemplos.







# Mathematics

Single dollars ($) are required for inline mathematics e.g. $f(x) = e^{\pi/x}$

Double dollars make self-standing equations:

$$\Theta(x) = \left\{\begin{array}{l}
0\textrm{ if } x < 0\cr
1\textrm{ else}
\end{array}\right.$$

You can also use plain \LaTeX for equations
\begin{equation}\label{eq:fourier}
\hat f(\omega) = \int_{-\infty}^{\infty} f(x) e^{i\omega x} dx
\end{equation}
and refer to \autoref{eq:fourier} from text.

# Citations

Citations to entries in paper.bib should be in
[rMarkdown](http://rmarkdown.rstudio.com/authoring_bibliographies_and_citations.html)
format.

If you want to cite a software repository URL (e.g. something on GitHub without a preferred
citation) then you can do it with the example BibTeX entry below for @fidgit.

For a quick reference, the following citation commands can be used:
- `@author:2001`  ->  "Author et al. (2001)"
- `[@author:2001]` -> "(Author et al., 2001)"
- `[@author1:2001; @author2:2001]` -> "(Author1 et al., 2001; Author2 et al., 2002)"

# Figures

Figures can be included like this:
![Caption for example figure.\label{fig:example}](figure.png)
and referenced from text using \autoref{fig:example}.

Figure sizes can be customized by adding an optional second parameter:
![Caption for example figure.](figure.png){ width=20% }

# Acknowledgements

We acknowledge contributions from Brigitta Sipocz, Syrtis Major, and Semyeong
Oh, and support from Kathryn Johnston during the genesis of this project.

# References


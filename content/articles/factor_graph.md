Title: Factor Graph
Date: Sat  2 Mar 19:09:52 CET 2019
Category: Math
Tags: Math

## High level problem definition and algorithm
Factor graph vs Pose graph

elimination
Sliding window, remove unrelated pose and constraints
marginalization, keep the size of graph constant while maintain the information.

Batch Estimation
Sliding window

## Software package
g2o vs ceres solver vs GTSAM vs AprilSAM vs iSAM
* 性能，维护，扩展升级性，依赖其他库
* Third party dependency:
* Sparse matrix, boost, eigen
* open source/free software Licence
	* LGPL vs GPL vs MIT vs BSD etc.
| package | Licence |
---|---
 CSPARSE | LGPL v2.1+
 Suitesparse | LGPL v3+
 g2o | BSD
 ceres | BSD
 Eigen < 3.1.1 | LGPL3+
 Eigen 3.1.1 | MPL2
 iSAM | LGPL v2.1+

## Hardware
performance requirements
* real-time
	* fast
	* predictability
* no OS?
* cache?

* SIMD, vectorization, compiler的局限, library
* multithreading
* multi-threaded BLAS
* 优化分层，先上层c/c++优化，再硬件优化，汇编优化
* profiling, performance bottleneck

## 项目管理
* git submodule, project system structure
git code review and repository management
commit notification, achieve, summary generation
gerrit ?
* sandbox user branch

review, validate and submit change
https://review.openstack.org/Documentation/intro-quick.html

CI jenkins
* project release branch
* project progress/ticket tracking
* project quality tracking
	* regression tracking
	* performance tracking
		* build time
		* runtime on given dataset



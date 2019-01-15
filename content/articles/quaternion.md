Title: 旋转矩阵，变化矩阵，旋转向量，欧拉角，四元数
Date: 2018-12-19
Category: Math
Tags: Math, SLAM

## 对比
* 平滑插值
* 紧凑
* 无奇异性
* 内存和运算速度更优。内存上，一个四元数只占四个浮点数；在四元数相乘时可以直接在这四个数上进行加减乘的基本运算，比旋转向量转换成旋转矩阵相乘后再转换回旋转向量要高效得多（Rodrigues 变换还涉及除法和三角函数等高级运算）。这些在嵌入式平台上是不小的优势。何况，浮点数运算总是会有误差的，运算越多，误差累计越多，所以理论上四元数相乘也有精度上的优势。

## transforms axis–angle coordinates to versors (unit quaternions):
the following expression transforms axis–angle coordinates to versors (unit quaternions):
$$Q=\left(\cos {\tfrac {\theta }{2}},{\boldsymbol {\omega }}\sin {\tfrac {\theta }{2}}\right)$$

## Recovering the axis-angle representation
Two rotation quaternions can be combined into one equivalent quaternion by the relation:
$\mathbf {q} '=\mathbf {q} _{2}\mathbf {q} _{1}$,
in which q′ corresponds to the rotation q1 followed by the rotation q2.
(Note that quaternion multiplication is not commutative.)

The expression $\mathbf {q} \mathbf {p} \mathbf {q} ^{-1}$ rotates any vector
quaternion $\mathbf {p}$ around an axis given by the vector a $\mathbf {a}$ by
the angle $\theta$, where a $\mathbf {a}$ and $\theta$ depends on the
quaternion $\mathbf {q} =q_{r}+q_{i}\mathbf {i} +q_{j}\mathbf {j} +q_{k}\mathbf {k}$

$\mathbf {a}$ and $\theta$ can be found from the following equations:
    $$ (a_{x},a_{y},a_{z})\ =\ {\frac {(q_{i},q_{j},q_{k})}{\sqrt {q_{i}^{2}+q_{j}^{2}+q_{k}^{2}}}}$$
    $$ \theta \ =\ 2\operatorname {atan2} \left({\sqrt {q_{i}^{2}+q_{j}^{2}+q_{k}^{2}}},q_{r}\right)$$
where $\mathrm {atan2}$ is the two-argument arctangent. Care should be taken when the quaternion approaches a scalar, since due to degeneracy the axis of an identity rotation is not well-defined

[CSDN总结](https://blog.csdn.net/EliminatedAcmer/article/details/81407176)

quaternion to axis–angle coordinates

```c++
inline Eigen::Vector3d toAngleAxis(const Eigen::Quaterniond& quaterd, double* angle=NULL)
{
	Eigen::Quaterniond unit_quaternion = quaterd.normalized();
	double n = unit_quaternion.vec().norm();
	double w = unit_quaternion.w();
	double squared_w = w*w;

	double two_atan_nbyw_by_n;
	// Atan-based log thanks to
	//
	// C. Hertzberg et al.:
	// "Integrating Generic Sensor Fusion Algorithms with Sound State
	// Representation through Encapsulation of Manifolds"
	// Information Fusion, 2011

	if (n < SMALL_EPS)
	{
		// If quaternion is normalized and n=1, then w should be 1;
		// w=0 should never happen here!
		assert(fabs(w)>SMALL_EPS);

		two_atan_nbyw_by_n = 2./w - 2.*(n*n)/(w*squared_w);
	}
	else
	{
		if (fabs(w)<SMALL_EPS)
		{
			if (w>0)
			{
				two_atan_nbyw_by_n = M_PI/n;
			}
			else
			{
				two_atan_nbyw_by_n = -M_PI/n;
			}
		}
		two_atan_nbyw_by_n = 2*atan(n/w)/n;
	}
	if(angle!=NULL) *angle = two_atan_nbyw_by_n*n;
	return two_atan_nbyw_by_n * unit_quaternion.vec();
}

inline Eigen::Quaterniond toQuaterniond(const Eigen::Vector3d& v3d, double* angle = NULL)
{
	double theta = v3d.norm();
	if(angle != NULL)
		*angle = theta;
	double half_theta = 0.5*theta;

	double imag_factor;
	double real_factor = cos(half_theta);
	if(theta<SMALL_EPS)
	{
		double theta_sq = theta*theta;
		double theta_po4 = theta_sq*theta_sq;
		imag_factor = 0.5-0.0208333*theta_sq+0.000260417*theta_po4;
	}
	else
	{
		double sin_half_theta = sin(half_theta);
		imag_factor = sin_half_theta/theta;
	}

	return Eigen::Quaterniond(real_factor,
			imag_factor*v3d.x(),
			imag_factor*v3d.y(),
			imag_factor*v3d.z());
}

SOPHUS_FUNC static SO3<Scalar> expAndTheta(Tangent const& omega,
		Scalar* theta) {
	SOPHUS_ENSURE(theta != nullptr, "must not be nullptr.");
	using std::abs;
	using std::cos;
	using std::sin;
	using std::sqrt;
	Scalar theta_sq = omega.squaredNorm();
	*theta = sqrt(theta_sq);
	Scalar half_theta = Scalar(0.5) * (*theta);

	Scalar imag_factor;
	Scalar real_factor;
	if ((*theta) < Constants<Scalar>::epsilon()) {
		Scalar theta_po4 = theta_sq * theta_sq;
		imag_factor = Scalar(0.5) - Scalar(1.0 / 48.0) * theta_sq +
			Scalar(1.0 / 3840.0) * theta_po4;
		real_factor = Scalar(1) - Scalar(1.0 / 8.0) * theta_sq +
			Scalar(1.0 / 384.0) * theta_po4;
	} else {
		Scalar sin_half_theta = sin(half_theta);
		imag_factor = sin_half_theta / (*theta);
		real_factor = cos(half_theta);
	}

	SO3 q;
	q.unit_quaternion_nonconst() =
		QuaternionMember(real_factor, imag_factor * omega.x(),
				imag_factor * omega.y(), imag_factor * omega.z());
	SOPHUS_ENSURE(abs(q.unit_quaternion().squaredNorm() - Scalar(1)) <
			Sophus::Constants<Scalar>::epsilon(),
			"SO3::exp failed! omega: %, real: %, img: %",
			omega.transpose(), real_factor, imag_factor);
	return q;
}

SOPHUS_FUNC TangentAndTheta logAndTheta() const {
	TangentAndTheta J;
	using std::abs;
	using std::atan;
	using std::sqrt;
	Scalar squared_n = unit_quaternion().vec().squaredNorm();
	Scalar n = sqrt(squared_n);
	Scalar w = unit_quaternion().w();

	Scalar two_atan_nbyw_by_n;

	// Atan-based log thanks to
	//
	// C. Hertzberg et al.:
	// "Integrating Generic Sensor Fusion Algorithms with Sound State
	// Representation through Encapsulation of Manifolds"
	// Information Fusion, 2011

	if (n < Constants<Scalar>::epsilon()) {
		// If quaternion is normalized and n=0, then w should be 1;
		// w=0 should never happen here!
		SOPHUS_ENSURE(abs(w) >= Constants<Scalar>::epsilon(),
				"Quaternion (%) should be normalized!",
				unit_quaternion().coeffs().transpose());
		Scalar squared_w = w * w;
		two_atan_nbyw_by_n =
			Scalar(2) / w - Scalar(2) * (squared_n) / (w * squared_w);
	} else {
		if (abs(w) < Constants<Scalar>::epsilon()) {
			if (w > Scalar(0)) {
				two_atan_nbyw_by_n = Constants<Scalar>::pi() / n;
			} else {
				two_atan_nbyw_by_n = -Constants<Scalar>::pi() / n;
			}
		} else {
			two_atan_nbyw_by_n = Scalar(2) * atan(n / w) / n;
		}
	}

	J.theta = two_atan_nbyw_by_n * n;

	J.tangent = two_atan_nbyw_by_n * unit_quaternion().vec();
	return J;
}
```







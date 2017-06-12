from .types import IntegrationType


class ChainingTimeStampF1D:
    """Class hierarchy: freestyle.types.UnaryFunction1D > freestyle.types.UnaryFunction1DVoid > freestyle.functions.ChainingTimeStampF1D"""

    def __init__(self):
        """Builds a ChainingTimeStampF1D object."""

    def __call__(self, inter):
        """Sets the chaining time stamp of the Interface1D.
        
        :param inter: An Interface1D object.
        :type inter: freestyle.types.Interface1D
        """


class Curvature2DAngleF0D:
    """Class hierarchy: freestyle.types.UnaryFunction0D > freestyle.types.UnaryFunction0DDouble > freestyle.functions.Curvature2DAngleF0D"""

    def __init__(self):
        """Builds a Curvature2DAngleF0D object."""

    def __call__(self, it):
        """Returns a real value giving the 2D curvature (as an angle) of the 1D
                                    element to which the freestyle.types.Interface0D pointed by
                                    the Interface0DIterator belongs.  The 2D curvature is evaluated at the
                                    Interface0D.
        
        :param it: An Interface0DIterator object.
        :type it: freestyle.types.Interface0DIterator
        :return: The 2D curvature of the 1D element evaluated at the
                                                    pointed Interface0D.
        :rtype: float
        """


class Curvature2DAngleF1D:
    """Class hierarchy: freestyle.types.UnaryFunction1D > freestyle.types.UnaryFunction1DDouble > freestyle.functions.Curvature2DAngleF1D"""

    def __init__(self, integration_type=IntegrationType.MEAN):
        """Builds a Curvature2DAngleF1D object.
        
        :param integration_type: The integration method used to compute a single value
                                                    from a set of values.
        :type integration_type: freestyle.types.IntegrationType
        """

    def __call__(self, inter):
        """Returns the 2D curvature as an angle for an Interface1D.
        
        :param inter: An Interface1D object.
        :type inter: freestyle.types.Interface1D
        :return: The 2D curvature as an angle.
        :rtype: float
        """


class CurveMaterialF0D:
    """A replacement of the built-in MaterialF0D for stroke creation.
                        MaterialF0D does not work with Curves and Strokes.  Line color
                        priority is used to pick one of the two materials at material
                        boundaries.
    """


class CurveNatureF0D:
    """Class hierarchy: freestyle.types.UnaryFunction0D > freestyle.types.UnaryFunction0DEdgeNature > freestyle.functions.CurveNatureF0D"""

    def __init__(self):
        """Builds a CurveNatureF0D object."""

    def __call__(self, it):
        """Returns the freestyle.types.Nature of the 1D element the
                                    Interface0D pointed by the Interface0DIterator belongs to.
        
        :param it: An Interface0DIterator object.
        :type it: freestyle.types.Interface0DIterator
        :return: The nature of the 1D element to which the pointed Interface0D
                                                    belongs.
        :rtype: freestyle.types.Nature
        """


class CurveNatureF1D:
    """Class hierarchy: freestyle.types.UnaryFunction1D > freestyle.types.UnaryFunction1DEdgeNature > freestyle.functions.CurveNatureF1D"""

    def __init__(self, integration_type=IntegrationType.MEAN):
        """Builds a CurveNatureF1D object.
        
        :param integration_type: The integration method used to compute a single value
                                                    from a set of values.
        :type integration_type: freestyle.types.IntegrationType
        """

    def __call__(self, inter):
        """Returns the nature of the Interface1D (silhouette, ridge, crease, and
                                    so on).  Except if the Interface1D is a
                                    freestyle.types.ViewEdge, this result might be ambiguous.
                                    Indeed, the Interface1D might result from the gathering of several 1D
                                    elements, each one being of a different nature.  An integration
                                    method, such as the MEAN, might give, in this case, irrelevant
                                    results.
        
        :param inter: An Interface1D object.
        :type inter: freestyle.types.Interface1D
        :return: The nature of the Interface1D.
        :rtype: freestyle.types.Nature
        """


class DensityF0D:
    """Class hierarchy: freestyle.types.UnaryFunction0D > freestyle.types.UnaryFunction0DDouble > freestyle.functions.DensityF0D"""

    def __init__(self, sigma=2.0):
        """Builds a DensityF0D object.
        
        :param sigma: The gaussian sigma value indicating the X value for
                                                    which the gaussian function is 0.5.  It leads to the window size
                                                    value (the larger, the smoother).
        :type sigma: float
        """

    def __call__(self, it):
        """Returns the density of the (result) image evaluated at the
                                    freestyle.types.Interface0D pointed by the
                                    Interface0DIterator. This density is evaluated using a pixels square
                                    window around the evaluation point and integrating these values using
                                    a gaussian.
        
        :param it: An Interface0DIterator object.
        :type it: freestyle.types.Interface0DIterator
        :return: The density of the image evaluated at the pointed
                                                    Interface0D.
        :rtype: float
        """


class DensityF1D:
    """Class hierarchy: freestyle.types.UnaryFunction1D > freestyle.types.UnaryFunction1DDouble > freestyle.functions.DensityF1D"""

    def __init__(self, sigma=2.0, integration_type=IntegrationType.MEAN, sampling=2.0):
        """Builds a DensityF1D object.
        
        :param sigma: The sigma used in DensityF0D and determining the window size
                                                            used in each density query.
        :type sigma: float
        :param integration_type: The integration method used to compute a single value
                                                            from a set of values.
        :type integration_type: freestyle.types.IntegrationType
        :param sampling: The resolution used to sample the chain: the
                                                            corresponding 0D function is evaluated at each sample point and
                                                            the result is obtained by combining the resulting values into a
                                                            single one, following the method specified by integration_type.
        :type sampling: float
        """

    def __call__(self, inter):
        """Returns the density evaluated for an Interface1D. The density is
                                    evaluated for a set of points along the Interface1D (using the
                                    freestyle.functions.DensityF0D functor) with a user-defined
                                    sampling and then integrated into a single value using a user-defined
                                    integration method.
        
        :param inter: An Interface1D object.
        :type inter: freestyle.types.Interface1D
        :return: The density evaluated for an Interface1D.
        :rtype: float
        """


class GetCompleteViewMapDensityF1D:
    """Class hierarchy: freestyle.types.UnaryFunction1D > freestyle.types.UnaryFunction1DDouble > freestyle.functions.GetCompleteViewMapDensityF1D"""

    def __init__(self, level, integration_type=IntegrationType.MEAN, sampling=2.0):
        """Builds a GetCompleteViewMapDensityF1D object.
        
        :param level: The level of the pyramid from which the pixel must be
                                                            read.
        :type level: int
        :param integration_type: The integration method used to compute a single value
                                                            from a set of values.
        :type integration_type: freestyle.types.IntegrationType
        :param sampling: The resolution used to sample the chain: the
                                                            corresponding 0D function is evaluated at each sample point and
                                                            the result is obtained by combining the resulting values into a
                                                            single one, following the method specified by integration_type.
        :type sampling: float
        """

    def __call__(self, inter):
        """Returns the density evaluated for an Interface1D in the complete
                                    viewmap image.  The density is evaluated for a set of points along the
                                    Interface1D (using the
                                    freestyle.functions.ReadCompleteViewMapPixelF0D functor) and
                                    then integrated into a single value using a user-defined integration
                                    method.
        
        :param inter: An Interface1D object.
        :type inter: freestyle.types.Interface1D
        :return: The density evaluated for the Interface1D in the complete
                                                    viewmap image.
        :rtype: float
        """


class GetCurvilinearAbscissaF0D:
    """Class hierarchy: freestyle.types.UnaryFunction0D > freestyle.types.UnaryFunction0DFloat > freestyle.functions.GetCurvilinearAbscissaF0D"""

    def __init__(self):
        """Builds a GetCurvilinearAbscissaF0D object."""

    def __call__(self, it):
        """Returns the curvilinear abscissa of the
                                    freestyle.types.Interface0D pointed by the
                                    Interface0DIterator in the context of its 1D element.
        
        :param it: An Interface0DIterator object.
        :type it: freestyle.types.Interface0DIterator
        :return: The curvilinear abscissa of the pointed Interface0D.
        :rtype: float
        """


class GetDirectionalViewMapDensityF1D:
    """Class hierarchy: freestyle.types.UnaryFunction1D > freestyle.types.UnaryFunction1DDouble > freestyle.functions.GetDirectionalViewMapDensityF1D"""

    def __init__(self, orientation, level, integration_type=IntegrationType.MEAN, sampling=2.0):
        """Builds a GetDirectionalViewMapDensityF1D object.
        
        :param orientation: The number of the directional map we must work
                                                            with.
        :type orientation: int
        :param level: The level of the pyramid from which the pixel must be
                                                            read.
        :type level: int
        :param integration_type: The integration method used to compute a single value
                                                            from a set of values.
        :type integration_type: freestyle.types.IntegrationType
        :param sampling: The resolution used to sample the chain: the
                                                            corresponding 0D function is evaluated at each sample point and
                                                            the result is obtained by combining the resulting values into a
                                                            single one, following the method specified by integration_type.
        :type sampling: float
        """

    def __call__(self, inter):
        """Returns the density evaluated for an Interface1D in of the steerable
                                    viewmaps image.  The direction telling which Directional map to choose
                                    is explicitly specified by the user.  The density is evaluated for a
                                    set of points along the Interface1D (using the
                                    freestyle.functions.ReadSteerableViewMapPixelF0D functor) and
                                    then integrated into a single value using a user-defined integration
                                    method.
        
        :param inter: An Interface1D object.
        :type inter: freestyle.types.Interface1D
        :return: the density evaluated for an Interface1D in of the
                                                    steerable viewmaps image.
        :rtype: float
        """


class GetOccludeeF0D:
    """Class hierarchy: freestyle.types.UnaryFunction0D > freestyle.types.UnaryFunction0DViewShape > freestyle.functions.GetOccludeeF0D"""

    def __init__(self):
        """Builds a GetOccludeeF0D object."""

    def __call__(self, it):
        """Returns the freestyle.types.ViewShape that the Interface0D
                                    pointed by the Interface0DIterator occludes.
        
        :param it: An Interface0DIterator object.
        :type it: freestyle.types.Interface0DIterator
        :return: The ViewShape occluded by the pointed Interface0D.
        :rtype: freestyle.types.ViewShape
        """


class GetOccludeeF1D:
    """Class hierarchy: freestyle.types.UnaryFunction1D > freestyle.types.UnaryFunction1DVectorViewShape > freestyle.functions.GetOccludeeF1D"""

    def __init__(self):
        """Builds a GetOccludeeF1D object."""

    def __call__(self, inter):
        """Returns a list of occluded shapes covered by this Interface1D.
        
        :param inter: An Interface1D object.
        :type inter: freestyle.types.Interface1D
        :return: A list of occluded shapes covered by the Interface1D.
        :param : (type: list of freestyle.types.ViewShape objects)
        :rtype: list
        """


class GetOccludersF0D:
    """Class hierarchy: freestyle.types.UnaryFunction0D > freestyle.types.UnaryFunction0DVectorViewShape > freestyle.functions.GetOccludersF0D"""

    def __init__(self):
        """Builds a GetOccludersF0D object."""

    def __call__(self, it):
        """Returns a list of freestyle.types.ViewShape objects occluding the
                                    freestyle.types.Interface0D pointed by the Interface0DIterator.
        
        :param it: An Interface0DIterator object.
        :type it: freestyle.types.Interface0DIterator
        :return: A list of ViewShape objects occluding the pointed
                                                    Interface0D.
        :param : (type: list of freestyle.types.ViewShape objects)
        :rtype: list
        """


class GetOccludersF1D:
    """Class hierarchy: freestyle.types.UnaryFunction1D > freestyle.types.UnaryFunction1DVectorViewShape > freestyle.functions.GetOccludersF1D"""

    def __init__(self):
        """Builds a GetOccludersF1D object."""

    def __call__(self, inter):
        """Returns a list of occluding shapes that cover this Interface1D.
        
        :param inter: An Interface1D object.
        :type inter: freestyle.types.Interface1D
        :return: A list of occluding shapes that cover the Interface1D.
        :param : (type: list of freestyle.types.ViewShape objects)
        :rtype: list
        """


class GetParameterF0D:
    """Class hierarchy: freestyle.types.UnaryFunction0D > freestyle.types.UnaryFunction0DFloat > freestyle.functions.GetParameterF0D"""

    def __init__(self):
        """Builds a GetParameterF0D object."""

    def __call__(self, it):
        """Returns the parameter of the freestyle.types.Interface0D
                                    pointed by the Interface0DIterator in the context of its 1D element.
        
        :param it: An Interface0DIterator object.
        :type it: freestyle.types.Interface0DIterator
        :return: The parameter of an Interface0D.
        :rtype: float
        """


class GetProjectedXF0D:
    """Class hierarchy: freestyle.types.UnaryFunction0D > freestyle.types.UnaryFunction0DDouble > freestyle.functions.GetProjectedXF0D"""

    def __init__(self):
        """Builds a GetProjectedXF0D object."""

    def __call__(self, it):
        """Returns the X 3D projected coordinate of the freestyle.types.Interface0D
                                    pointed by the Interface0DIterator.
        
        :param it: An Interface0DIterator object.
        :type it: freestyle.types.Interface0DIterator
        :return: The X 3D projected coordinate of the pointed Interface0D.
        :rtype: float
        """


class GetProjectedXF1D:
    """Class hierarchy: freestyle.types.UnaryFunction1D > freestyle.types.UnaryFunction1DDouble > freestyle.functions.GetProjectedXF1D"""

    def __init__(self, integration_type=IntegrationType.MEAN):
        """Builds a GetProjectedXF1D object.
        
        :param integration_type: The integration method used to compute a single value
                                                    from a set of values.
        :type integration_type: freestyle.types.IntegrationType
        """

    def __call__(self, inter):
        """Returns the projected X 3D coordinate of an Interface1D.
        
        :param inter: An Interface1D object.
        :type inter: freestyle.types.Interface1D
        :return: The projected X 3D coordinate of an Interface1D.
        :rtype: float
        """


class GetProjectedYF0D:
    """Class hierarchy: freestyle.types.UnaryFunction0D > freestyle.types.UnaryFunction0DDouble > freestyle.functions.GetProjectedYF0D"""

    def __init__(self):
        """Builds a GetProjectedYF0D object."""

    def __call__(self, it):
        """Returns the Y 3D projected coordinate of the freestyle.types.Interface0D
                                    pointed by the Interface0DIterator.
        
        :param it: An Interface0DIterator object.
        :type it: freestyle.types.Interface0DIterator
        :return: The Y 3D projected coordinate of the pointed Interface0D.
        :rtype: float
        """


class GetProjectedYF1D:
    """Class hierarchy: freestyle.types.UnaryFunction1D > freestyle.types.UnaryFunction1DDouble > freestyle.functions.GetProjectedYF1D"""

    def __init__(self, integration_type=IntegrationType.MEAN):
        """Builds a GetProjectedYF1D object.
        
        :param integration_type: The integration method used to compute a single value
                                                    from a set of values.
        :type integration_type: freestyle.types.IntegrationType
        """

    def __call__(self, inter):
        """Returns the projected Y 3D coordinate of an Interface1D.
        
        :param inter: An Interface1D object.
        :type inter: freestyle.types.Interface1D
        :return: The projected Y 3D coordinate of an Interface1D.
        :rtype: float
        """


class GetProjectedZF0D:
    """Class hierarchy: freestyle.types.UnaryFunction0D > freestyle.types.UnaryFunction0DDouble > freestyle.functions.GetProjectedZF0D"""

    def __init__(self):
        """Builds a GetProjectedZF0D object."""

    def __call__(self, it):
        """Returns the Z 3D projected coordinate of the freestyle.types.Interface0D
                                    pointed by the Interface0DIterator.
        
        :param it: An Interface0DIterator object.
        :type it: freestyle.types.Interface0DIterator
        :return: The Z 3D projected coordinate of the pointed Interface0D.
        :rtype: float
        """


class GetProjectedZF1D:
    """Class hierarchy: freestyle.types.UnaryFunction1D > freestyle.types.UnaryFunction1DDouble > freestyle.functions.GetProjectedZF1D"""

    def __init__(self, integration_type=IntegrationType.MEAN):
        """Builds a GetProjectedZF1D object.
        
        :param integration_type: The integration method used to compute a single value
                                                    from a set of values.
        :type integration_type: freestyle.types.IntegrationType
        """

    def __call__(self, inter):
        """Returns the projected Z 3D coordinate of an Interface1D.
        
        :param inter: An Interface1D object.
        :type inter: freestyle.types.Interface1D
        :return: The projected Z 3D coordinate of an Interface1D.
        :rtype: float
        """


class GetShapeF0D:
    """Class hierarchy: freestyle.types.UnaryFunction0D > freestyle.types.UnaryFunction0DViewShape > freestyle.functions.GetShapeF0D"""

    def __init__(self):
        """Builds a GetShapeF0D object."""

    def __call__(self, it):
        """Returns the freestyle.types.ViewShape containing the
                                    Interface0D pointed by the Interface0DIterator.
        
        :param it: An Interface0DIterator object.
        :type it: freestyle.types.Interface0DIterator
        :return: The ViewShape containing the pointed Interface0D.
        :rtype: freestyle.types.ViewShape
        """


class GetShapeF1D:
    """Class hierarchy: freestyle.types.UnaryFunction1D > freestyle.types.UnaryFunction1DVectorViewShape > freestyle.functions.GetShapeF1D"""

    def __init__(self):
        """Builds a GetShapeF1D object."""

    def __call__(self, inter):
        """Returns a list of shapes covered by this Interface1D.
        
        :param inter: An Interface1D object.
        :type inter: freestyle.types.Interface1D
        :return: A list of shapes covered by the Interface1D.
        :param : (type: list of freestyle.types.ViewShape objects)
        :rtype: list
        """


class GetSteerableViewMapDensityF1D:
    """Class hierarchy: freestyle.types.UnaryFunction1D > freestyle.types.UnaryFunction1DDouble > freestyle.functions.GetSteerableViewMapDensityF1D"""

    def __init__(self, level, integration_type=IntegrationType.MEAN, sampling=2.0):
        """Builds a GetSteerableViewMapDensityF1D object.
        
        :param level: The level of the pyramid from which the pixel must be
                                                            read.
        :type level: int
        :param integration_type: The integration method used to compute a single value
                                                            from a set of values.
        :type integration_type: freestyle.types.IntegrationType
        :param sampling: The resolution used to sample the chain: the
                                                            corresponding 0D function is evaluated at each sample point and
                                                            the result is obtained by combining the resulting values into a
                                                            single one, following the method specified by integration_type.
        :type sampling: float
        """

    def __call__(self, inter):
        """Returns the density of the ViewMap for a given Interface1D.  The
                                    density of each freestyle.types.FEdge is evaluated in the
                                    proper steerable freestyle.types.ViewMap depending on its
                                    orientation.
        
        :param inter: An Interface1D object.
        :type inter: freestyle.types.Interface1D
        :return: The density of the ViewMap for a given Interface1D.
        :rtype: float
        """


class GetViewMapGradientNormF0D:
    """Class hierarchy: freestyle.types.UnaryFunction0D > freestyle.types.UnaryFunction0DFloat > freestyle.functions.GetViewMapGradientNormF0D"""

    def __init__(self, level):
        """Builds a GetViewMapGradientNormF0D object.
        
        :param level: The level of the pyramid from which the pixel must be
                                                    read.
        :type level: int
        """

    def __call__(self, it):
        """Returns the norm of the gradient of the global viewmap density
                                    image.
        
        :param it: An Interface0DIterator object.
        :type it: freestyle.types.Interface0DIterator
        :return: The norm of the gradient of the global viewmap density
                                                    image.
        :rtype: float
        """


class GetViewMapGradientNormF1D:
    """Class hierarchy: freestyle.types.UnaryFunction1D > freestyle.types.UnaryFunction1DDouble > freestyle.functions.GetViewMapGradientNormF1D"""

    def __init__(self, level, integration_type=IntegrationType.MEAN, sampling=2.0):
        """Builds a GetViewMapGradientNormF1D object.
        
        :param level: The level of the pyramid from which the pixel must be
                                                            read.
        :type level: int
        :param integration_type: The integration method used to compute a single value
                                                            from a set of values.
        :type integration_type: freestyle.types.IntegrationType
        :param sampling: The resolution used to sample the chain: the
                                                            corresponding 0D function is evaluated at each sample point and
                                                            the result is obtained by combining the resulting values into a
                                                            single one, following the method specified by integration_type.
        :type sampling: float
        """

    def __call__(self, inter):
        """Returns the density of the ViewMap for a given Interface1D.  The
                                    density of each freestyle.types.FEdge is evaluated in the
                                    proper steerable freestyle.types.ViewMap depending on its
                                    orientation.
        
        :param inter: An Interface1D object.
        :type inter: freestyle.types.Interface1D
        :return: The density of the ViewMap for a given Interface1D.
        :rtype: float
        """


class GetXF0D:
    """Class hierarchy: freestyle.types.UnaryFunction0D > freestyle.types.UnaryFunction0DDouble > freestyle.functions.GetXF0D"""

    def __init__(self):
        """Builds a GetXF0D object."""

    def __call__(self, it):
        """Returns the X 3D coordinate of the freestyle.types.Interface0D pointed by
                                    the Interface0DIterator.
        
        :param it: An Interface0DIterator object.
        :type it: freestyle.types.Interface0DIterator
        :return: The X 3D coordinate of the pointed Interface0D.
        :rtype: float
        """


class GetXF1D:
    """Class hierarchy: freestyle.types.UnaryFunction1D > freestyle.types.UnaryFunction1DDouble > freestyle.functions.GetXF1D"""

    def __init__(self, integration_type=IntegrationType.MEAN):
        """Builds a GetXF1D object.
        
        :param integration_type: The integration method used to compute a single value
                                                    from a set of values.
        :type integration_type: freestyle.types.IntegrationType
        """

    def __call__(self, inter):
        """Returns the X 3D coordinate of an Interface1D.
        
        :param inter: An Interface1D object.
        :type inter: freestyle.types.Interface1D
        :return: The X 3D coordinate of the Interface1D.
        :rtype: float
        """


class GetYF0D:
    """Class hierarchy: freestyle.types.UnaryFunction0D > freestyle.types.UnaryFunction0DDouble > freestyle.functions.GetYF0D"""

    def __init__(self):
        """Builds a GetYF0D object."""

    def __call__(self, it):
        """Returns the Y 3D coordinate of the freestyle.types.Interface0D pointed by
                                    the Interface0DIterator.
        
        :param it: An Interface0DIterator object.
        :type it: freestyle.types.Interface0DIterator
        :return: The Y 3D coordinate of the pointed Interface0D.
        :rtype: float
        """


class GetYF1D:
    """Class hierarchy: freestyle.types.UnaryFunction1D > freestyle.types.UnaryFunction1DDouble > freestyle.functions.GetYF1D"""

    def __init__(self, integration_type=IntegrationType.MEAN):
        """Builds a GetYF1D object.
        
        :param integration_type: The integration method used to compute a single value
                                                    from a set of values.
        :type integration_type: freestyle.types.IntegrationType
        """

    def __call__(self, inter):
        """Returns the Y 3D coordinate of an Interface1D.
        
        :param inter: An Interface1D object.
        :type inter: freestyle.types.Interface1D
        :return: The Y 3D coordinate of the Interface1D.
        :rtype: float
        """


class GetZF0D:
    """Class hierarchy: freestyle.types.UnaryFunction0D > freestyle.types.UnaryFunction0DDouble > freestyle.functions.GetZF0D"""

    def __init__(self):
        """Builds a GetZF0D object."""

    def __call__(self, it):
        """Returns the Z 3D coordinate of the freestyle.types.Interface0D pointed by
                                    the Interface0DIterator.
        
        :param it: An Interface0DIterator object.
        :type it: freestyle.types.Interface0DIterator
        :return: The Z 3D coordinate of the pointed Interface0D.
        :rtype: float
        """


class GetZF1D:
    """Class hierarchy: freestyle.types.UnaryFunction1D > freestyle.types.UnaryFunction1DDouble > freestyle.functions.GetZF1D"""

    def __init__(self, integration_type=IntegrationType.MEAN):
        """Builds a GetZF1D object.
        
        :param integration_type: The integration method used to compute a single value
                                                    from a set of values.
        :type integration_type: freestyle.types.IntegrationType
        """

    def __call__(self, inter):
        """Returns the Z 3D coordinate of an Interface1D.
        
        :param inter: An Interface1D object.
        :type inter: freestyle.types.Interface1D
        :return: The Z 3D coordinate of the Interface1D.
        :rtype: float
        """


class IncrementChainingTimeStampF1D:
    """Class hierarchy: freestyle.types.UnaryFunction1D > freestyle.types.UnaryFunction1DVoid > freestyle.functions.IncrementChainingTimeStampF1D"""

    def __init__(self):
        """Builds an IncrementChainingTimeStampF1D object."""

    def __call__(self, inter):
        """Increments the chaining time stamp of the Interface1D.
        
        :param inter: An Interface1D object.
        :type inter: freestyle.types.Interface1D
        """


class LocalAverageDepthF0D:
    """Class hierarchy: freestyle.types.UnaryFunction0D > freestyle.types.UnaryFunction0DDouble > freestyle.functions.LocalAverageDepthF0D"""

    def __init__(self, mask_size=5.0):
        """Builds a LocalAverageDepthF0D object.
        
        :param mask_size: The size of the mask.
        :type mask_size: float
        """

    def __call__(self, it):
        """Returns the average depth around the
                                    freestyle.types.Interface0D pointed by the
                                    Interface0DIterator.  The result is obtained by querying the depth
                                    buffer on a window around that point.
        
        :param it: An Interface0DIterator object.
        :type it: freestyle.types.Interface0DIterator
        :return: The average depth around the pointed Interface0D.
        :rtype: float
        """


class LocalAverageDepthF1D:
    """Class hierarchy: freestyle.types.UnaryFunction1D > freestyle.types.UnaryFunction1DDouble > freestyle.functions.LocalAverageDepthF1D"""

    def __init__(self, sigma, integration_type=IntegrationType.MEAN):
        """Builds a LocalAverageDepthF1D object.
        
        :param sigma: The sigma used in DensityF0D and determining the window
                                                            size used in each density query.
        :type sigma: float
        :param integration_type: The integration method used to compute a single value
                                                            from a set of values.
        :type integration_type: freestyle.types.IntegrationType
        """

    def __call__(self, inter):
        """Returns the average depth evaluated for an Interface1D.  The average
                                    depth is evaluated for a set of points along the Interface1D (using
                                    the freestyle.functions.LocalAverageDepthF0D functor) with a
                                    user-defined sampling and then integrated into a single value using a
                                    user-defined integration method.
        
        :param inter: An Interface1D object.
        :type inter: freestyle.types.Interface1D
        :return: The average depth evaluated for the Interface1D.
        :rtype: float
        """


class MaterialF0D:
    """Class hierarchy: freestyle.types.UnaryFunction0D > freestyle.types.UnaryFunction0DMaterial > freestyle.functions.MaterialF0D"""

    def __init__(self):
        """Builds a MaterialF0D object."""

    def __call__(self, it):
        """Returns the material of the object evaluated at the
                                    freestyle.types.Interface0D pointed by the
                                    Interface0DIterator.  This evaluation can be ambiguous (in the case of
                                    a freestyle.types.TVertex for example.  This functor tries to
                                    remove this ambiguity using the context offered by the 1D element to
                                    which the Interface0DIterator belongs to and by arbitrary choosing the
                                    material of the face that lies on its left when following the 1D
                                    element if there are two different materials on each side of the
                                    point.  However, there still can be problematic cases, and the user
                                    willing to deal with this cases in a specific way should implement its
                                    own getMaterial functor.
        
        :param it: An Interface0DIterator object.
        :type it: freestyle.types.Interface0DIterator
        :return: The material of the object evaluated at the pointed
                                                    Interface0D.
        :rtype: freestyle.types.Material
        """


class Normal2DF0D:
    """Class hierarchy: freestyle.types.UnaryFunction0D > freestyle.types.UnaryFunction0DVec2f > freestyle.functions.Normal2DF0D"""

    def __init__(self):
        """Builds a Normal2DF0D object."""

    def __call__(self, it):
        """Returns a two-dimensional vector giving the normalized 2D normal to
                                    the 1D element to which the freestyle.types.Interface0D
                                    pointed by the Interface0DIterator belongs.  The normal is evaluated
                                    at the pointed Interface0D.
        
        :param it: An Interface0DIterator object.
        :type it: freestyle.types.Interface0DIterator
        :return: The 2D normal of the 1D element evaluated at the pointed
                                                    Interface0D.
        :rtype: mathutils.Vector
        """


class Normal2DF1D:
    """Class hierarchy: freestyle.types.UnaryFunction1D > freestyle.types.UnaryFunction1DVec2f > freestyle.functions.Normal2DF1D"""

    def __init__(self, integration_type=IntegrationType.MEAN):
        """Builds a Normal2DF1D object.
        
        :param integration_type: The integration method used to compute a single value
                                                    from a set of values.
        :type integration_type: freestyle.types.IntegrationType
        """

    def __call__(self, inter):
        """Returns the 2D normal for the Interface1D.
        
        :param inter: An Interface1D object.
        :type inter: freestyle.types.Interface1D
        :return: The 2D normal for the Interface1D.
        :rtype: mathutils.Vector
        """


class Orientation2DF1D:
    """Class hierarchy: freestyle.types.UnaryFunction1D > freestyle.types.UnaryFunction1DVec2f > freestyle.functions.Orientation2DF1D"""

    def __init__(self, integration_type=IntegrationType.MEAN):
        """Builds an Orientation2DF1D object.
        
        :param integration_type: The integration method used to compute a single value
                                                    from a set of values.
        :type integration_type: freestyle.types.IntegrationType
        """

    def __call__(self, inter):
        """Returns the 2D orientation of the Interface1D.
        
        :param inter: An Interface1D object.
        :type inter: freestyle.types.Interface1D
        :return: The 2D orientation of the Interface1D.
        :rtype: mathutils.Vector
        """


class Orientation3DF1D:
    """Class hierarchy: freestyle.types.UnaryFunction1D > freestyle.types.UnaryFunction1DVec3f > freestyle.functions.Orientation3DF1D"""

    def __init__(self, integration_type=IntegrationType.MEAN):
        """Builds an Orientation3DF1D object.
        
        :param integration_type: The integration method used to compute a single value
                                                    from a set of values.
        :type integration_type: freestyle.types.IntegrationType
        """

    def __call__(self, inter):
        """Returns the 3D orientation of the Interface1D.
        
        :param inter: An Interface1D object.
        :type inter: freestyle.types.Interface1D
        :return: The 3D orientation of the Interface1D.
        :rtype: mathutils.Vector
        """


class QuantitativeInvisibilityF0D:
    """Class hierarchy: freestyle.types.UnaryFunction0D > freestyle.types.UnaryFunction0DUnsigned > freestyle.functions.QuantitativeInvisibilityF0D"""

    def __init__(self):
        """Builds a QuantitativeInvisibilityF0D object."""

    def __call__(self, it):
        """Returns the quantitative invisibility of the
                                    freestyle.types.Interface0D pointed by the
                                    Interface0DIterator.  This evaluation can be ambiguous (in the case of
                                    a freestyle.types.TVertex for example).  This functor tries
                                    to remove this ambiguity using the context offered by the 1D element
                                    to which the Interface0D belongs to.  However, there still can be
                                    problematic cases, and the user willing to deal with this cases in a
                                    specific way should implement its own getQIF0D functor.
        
        :param it: An Interface0DIterator object.
        :type it: freestyle.types.Interface0DIterator
        :return: The quantitative invisibility of the pointed Interface0D.
        :rtype: int
        """


class QuantitativeInvisibilityF1D:
    """Class hierarchy: freestyle.types.UnaryFunction1D > freestyle.types.UnaryFunction1DUnsigned > freestyle.functions.QuantitativeInvisibilityF1D"""

    def __init__(self, integration_type=IntegrationType.MEAN):
        """Builds a QuantitativeInvisibilityF1D object.
        
        :param integration_type: The integration method used to compute a single value
                                                    from a set of values.
        :type integration_type: freestyle.types.IntegrationType
        """

    def __call__(self, inter):
        """Returns the Quantitative Invisibility of an Interface1D element. If
                                    the Interface1D is a freestyle.types.ViewEdge, then there is
                                    no ambiguity concerning the result.  But, if the Interface1D results
                                    of a chaining (chain, stroke), then it might be made of several 1D
                                    elements of different Quantitative Invisibilities.
        
        :param inter: An Interface1D object.
        :type inter: freestyle.types.Interface1D
        :return: The Quantitative Invisibility of the Interface1D.
        :rtype: int
        """


class ReadCompleteViewMapPixelF0D:
    """Class hierarchy: freestyle.types.UnaryFunction0D > freestyle.types.UnaryFunction0DFloat > freestyle.functions.ReadCompleteViewMapPixelF0D"""

    def __init__(self, level):
        """Builds a ReadCompleteViewMapPixelF0D object.
        
        :param level: The level of the pyramid from which the pixel must be
                                                    read.
        :type level: int
        """

    def __call__(self, it):
        """Reads a pixel in one of the level of the complete viewmap.
        
        :param it: An Interface0DIterator object.
        :type it: freestyle.types.Interface0DIterator
        :return: A pixel in one of the level of the complete viewmap.
        :rtype: float
        """


class ReadMapPixelF0D:
    """Class hierarchy: freestyle.types.UnaryFunction0D > freestyle.types.UnaryFunction0DFloat > freestyle.functions.ReadMapPixelF0D"""

    def __init__(self, map_name, level):
        """Builds a ReadMapPixelF0D object.
        
        :param map_name: The name of the map to be read.
        :type map_name: str
        :param level: The level of the pyramid from which the pixel must be
                                                            read.
        :type level: int
        """

    def __call__(self, it):
        """Reads a pixel in a map.
        
        :param it: An Interface0DIterator object.
        :type it: freestyle.types.Interface0DIterator
        :return: A pixel in a map.
        :rtype: float
        """


class ReadSteerableViewMapPixelF0D:
    """Class hierarchy: freestyle.types.UnaryFunction0D > freestyle.types.UnaryFunction0DFloat > freestyle.functions.ReadSteerableViewMapPixelF0D"""

    def __init__(self, orientation, level):
        """Builds a ReadSteerableViewMapPixelF0D object.
        
        :param orientation: The integer belonging to [0, 4] indicating the
                                                            orientation (E, NE, N, NW) we are interested in.
        :type orientation: int
        :param level: The level of the pyramid from which the pixel must be
                                                            read.
        :type level: int
        """

    def __call__(self, it):
        """Reads a pixel in one of the level of one of the steerable viewmaps.
        
        :param it: An Interface0DIterator object.
        :type it: freestyle.types.Interface0DIterator
        :return: A pixel in one of the level of one of the steerable viewmaps.
        :rtype: float
        """


class ShapeIdF0D:
    """Class hierarchy: freestyle.types.UnaryFunction0D > freestyle.types.UnaryFunction0DId > freestyle.functions.ShapeIdF0D"""

    def __init__(self):
        """Builds a ShapeIdF0D object."""

    def __call__(self, it):
        """Returns the freestyle.types.Id of the Shape the
                                    freestyle.types.Interface0D pointed by the
                                    Interface0DIterator belongs to. This evaluation can be ambiguous (in
                                    the case of a freestyle.types.TVertex for example).  This
                                    functor tries to remove this ambiguity using the context offered by
                                    the 1D element to which the Interface0DIterator belongs to. However,
                                    there still can be problematic cases, and the user willing to deal
                                    with this cases in a specific way should implement its own
                                    getShapeIdF0D functor.
        
        :param it: An Interface0DIterator object.
        :type it: freestyle.types.Interface0DIterator
        :return: The Id of the Shape the pointed Interface0D belongs to.
        :rtype: freestyle.types.Id
        """


class TimeStampF1D:
    """Class hierarchy: freestyle.types.UnaryFunction1D > freestyle.types.UnaryFunction1DVoid > freestyle.functions.TimeStampF1D"""

    def __init__(self):
        """Builds a TimeStampF1D object."""

    def __call__(self, inter):
        """Returns the time stamp of the Interface1D.
        
        :param inter: An Interface1D object.
        :type inter: freestyle.types.Interface1D
        """


class VertexOrientation2DF0D:
    """Class hierarchy: freestyle.types.UnaryFunction0D > freestyle.types.UnaryFunction0DVec2f > freestyle.functions.VertexOrientation2DF0D"""

    def __init__(self):
        """Builds a VertexOrientation2DF0D object."""

    def __call__(self, it):
        """Returns a two-dimensional vector giving the 2D oriented tangent to the
                                    1D element to which the freestyle.types.Interface0D pointed
                                    by the Interface0DIterator belongs.  The 2D oriented tangent is
                                    evaluated at the pointed Interface0D.
        
        :param it: An Interface0DIterator object.
        :type it: freestyle.types.Interface0DIterator
        :return: The 2D oriented tangent to the 1D element evaluated at the
                                                    pointed Interface0D.
        :rtype: mathutils.Vector
        """


class VertexOrientation3DF0D:
    """Class hierarchy: freestyle.types.UnaryFunction0D > freestyle.types.UnaryFunction0DVec3f > freestyle.functions.VertexOrientation3DF0D"""

    def __init__(self):
        """Builds a VertexOrientation3DF0D object."""

    def __call__(self, it):
        """Returns a three-dimensional vector giving the 3D oriented tangent to
                                    the 1D element to which the freestyle.types.Interface0D
                                    pointed by the Interface0DIterator belongs.  The 3D oriented tangent
                                    is evaluated at the pointed Interface0D.
        
        :param it: An Interface0DIterator object.
        :type it: freestyle.types.Interface0DIterator
        :return: The 3D oriented tangent to the 1D element evaluated at the
                                                    pointed Interface0D.
        :rtype: mathutils.Vector
        """


class ZDiscontinuityF0D:
    """Class hierarchy: freestyle.types.UnaryFunction0D > freestyle.types.UnaryFunction0DDouble > freestyle.functions.ZDiscontinuityF0D"""

    def __init__(self):
        """Builds a ZDiscontinuityF0D object."""

    def __call__(self, it):
        """Returns a real value giving the distance between the
                                    freestyle.types.Interface0D pointed by the
                                    Interface0DIterator and the shape that lies behind (occludee).  This
                                    distance is evaluated in the camera space and normalized between 0 and
                                    1.  Therefore, if no object is occluded by the shape to which the
                                    Interface0D belongs to, 1 is returned.
        
        :param it: An Interface0DIterator object.
        :type it: freestyle.types.Interface0DIterator
        :return: The normalized distance between the pointed Interface0D
                                                    and the occludee.
        :rtype: float
        """


class ZDiscontinuityF1D:
    """Class hierarchy: freestyle.types.UnaryFunction1D > freestyle.types.UnaryFunction1DDouble > freestyle.functions.ZDiscontinuityF1D"""

    def __init__(self, integration_type=IntegrationType.MEAN):
        """Builds a ZDiscontinuityF1D object.
        
        :param integration_type: The integration method used to compute a single value
                                                    from a set of values.
        :type integration_type: freestyle.types.IntegrationType
        """

    def __call__(self, inter):
        """Returns a real value giving the distance between an Interface1D
                                    and the shape that lies behind (occludee).  This distance is
                                    evaluated in the camera space and normalized between 0 and 1.
                                    Therefore, if no object is occluded by the shape to which the
                                    Interface1D belongs to, 1 is returned.
        
        :param inter: An Interface1D object.
        :type inter: freestyle.types.Interface1D
        :return: The normalized distance between the Interface1D and the occludee.
        :rtype: float
        """


class pyCurvilinearLengthF0D:
    """"""


class pyDensityAnisotropyF0D:
    """Estimates the anisotropy of density."""


class pyDensityAnisotropyF1D:
    """"""


class pyGetInverseProjectedZF1D:
    """"""


class pyGetSquareInverseProjectedZF1D:
    """"""


class pyInverseCurvature2DAngleF0D:
    """"""


class pyViewMapGradientNormF0D:
    """"""


class pyViewMapGradientNormF1D:
    """"""


class pyViewMapGradientVectorF0D:
    """Returns the gradient vector for a pixel."""

    def __init__(self, level):
        """Builds a pyViewMapGradientVectorF0D object.
        
        :param level: the level at which to compute the gradient
        :type level: int
        """

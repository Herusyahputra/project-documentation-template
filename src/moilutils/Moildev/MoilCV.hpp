#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <cassert>

#include <iostream>
#include <string.h>
#include <math.h>

#define PI 3.1415926
#define PCT_UNIT_WIDTH 1.27
#define PCT_UNIT_HEIGHT 1.27
#define FOCAL_LENGTH_FOR_ZOOM 250

using namespace std;
namespace py = pybind11;

void test(){
        cout <<"-- Help!!\n  Thank for using Moildev-SDK..\n  For more information, Please visit https://github.com/MoilOrg/moildev\n  All copyrights reserved to Moil-Lab\n";
    }

void version(){
        cout <<"===========================================\nName: Moildev-SDK for Python3 \nVersion: 3.1.0 \nLast Update: 04 May 2022\nAuthor: Moil-Lab \nWriter: Haryanto \nAuthor-Email: haryanto@o365.mcut.edu.tw\nUnder license: Moil-Lab\n===========================================\n";
    }

class MoilCV {
    public:
        // Factory function:
        MoilCV (string &name,  double cswidth,double csheight, double Icx, double Icy,
            double Ratio, double ImWidth, double ImHeight,double calibRatio, double Para0, double Para1,
            double Para2, double Para3, double Para4, double Para5);
        ~ MoilCV();
//        void fish_rotate(unsigned char *dst, unsigned char *src, int cols, int rows, double c0, double r0, double degree) ;
        double AnyPointM(py::array_t<float> array, py::array_t<float> arrayb, double alphaOffset, double betaOffset, double zoom);
        double AnyPointM2(py::array_t<float> array, py::array_t<float> arrayb, double thetaX_degree, double thetaY_degree, double zoom);
        double alpha2IH(double p_alpha_in_rad);
        double PanoramaX(py::array_t<float> array, py::array_t<float> arrayb, double alpha_max, double min);
        double PanoramaM_Rt(py::array_t<float> array, py::array_t<float> arrayb, double alpha_max, double iC_alpha_degree, double iC_beta_degree);
        double anypointImageModeM(py::array_t<uint8_t> src, py::array_t<uint8_t> dst, double alphaOffset, double betaOffset, double zoom);
        double CarAnyPoint(py::array_t<float> array, py::array_t<float> arrayb,
                    double pch_azm_pivot,
                    double yaw_zth_pivot,
                    double cj_roll_degree,
                    double zoom);
        double NewAnyPointM(py::array_t<float> array, py::array_t<float> arrayb,
                             double alphaOffset,
                             double betaOffset,
                             double zoom);
        double AnyPoint_M_M(py::array_t<float> array, py::array_t<float> arrayb,
                    double pch_azm_pivot,
                    double yaw_zth_pivot,
                    double cj_roll_degree,
                    double zoom,
                    void (*fun_euler_rotate)(const double c1, const double s1, const double c2, const double s2, const double c3,
                                                     const double s3, double uX, double uY, double uZ, double &tempX, double &tempY,
                                                     double &tempZ));
        double xPanoramaM_Rt(py::array_t<float> array, py::array_t<float> arrayb,
                                double my_p_alpha_max_vendor,
                                double p_iC_alpha_degree, double p_iC_beta_degree,
                                double p_alpha_from, double p_alpha_end);
//        void MoilCV::fish_rotate(py::array_t<uint8_t> src, py::array_t<uint8_t> dst, double degree);
        double revPanorama(py::array_t<uint8_t> array, py::array_t<uint8_t> arrayb, double alpha_max, double beta_offset);
        double revPanoramaMaps(py::array_t<float> array, py::array_t<float> arrayb, double alpha_max, double beta_offset);
        double alpha_ih_vga(double p_alpha_in_rad) const;
        void initAlphaRho_Table();
        int getRhoFromAlpha( double alpha );
        double getAlphaFromRho( int rho );

    private:
        string camera_Name ;
        double camera_SensorWidth ;
        double camera_SensorHeight ;
        double camera_iCx ;
        double camera_iCy ;
        double camera_ratio ;
        double camera_imageWidth ;
        double camera_imageHeight ;
        double camera_calibrationRatio ;
        double camera_para0 ;
        double camera_para1 ;
        double camera_para2 ;
        double camera_para3 ;
        double camera_para4 ;
        double camera_para5 ;
        int alphaToRho_Table[1800];
        int rhoToAlpha_Table[3600];
};

PYBIND11_MODULE(MoilCV, m){
    // optional module docstring
    m.doc() = "pybind11 example plugin";
    m.def("test", &test, "Show Help from this library");
    m.def("version", &version, "Show Information about Moildev SDK");

    py::class_<MoilCV>(m, "MoilCV")
        .def(py::init<string &, double,double,double,double,double, double,
                double,double,double,double,double,double,
                double,double>(), "This is the initial configuration that you need provide the parameter. \n"
                                  "The camera parameter is the result from calibration camera by MOIL laboratory. \n"
                                  "Before the successive functions can work correctly,configuration is necessary \n"
                                  "in the beginning of program. \n\n "
                                  "Args:\n"
                                    ". camera_name - A string to describe this camera\n"
                                    ". sensor_width - Camera sensor width (cm)\n"
                                    ". sensor_height - Camera Sensor Height (cm)\n"
                                    ". Icx - image center X coordinate(pixel)\n"
                                    ". Icy - image center Y coordinate(pixel)\n"
                                    ". ratio : Sensor pixel aspect ratio.\n"
                                    ". imageWidth : Input image width\n"
                                    ". imageHeight : Input image height\n"
                                    ". calibrationRatio : input image with/ calibrationRation image width\n"
                                    ". parameter0 .. parameter5 : calibrationRation parameters\n"
                                 "for more detail, please reference https://github.com/MoilOrg/moildev")

        .def("AnyPointM", &MoilCV::AnyPointM)

        .def("anypointImageModeM", &MoilCV::anypointImageModeM)

        .def("AnyPointM2", &MoilCV::AnyPointM2)

        .def("CarAnyPoint", &MoilCV::CarAnyPoint)

        .def("NewAnyPointM", &MoilCV::NewAnyPointM)

//        .def("fish_rotate", &MoilCV::fish_rotate)

        .def("Panorama", &MoilCV::PanoramaX)

        .def("xPanoramaM_Rt", &MoilCV::xPanoramaM_Rt)

        .def("PanoramaM_Rt", &MoilCV::PanoramaM_Rt)

        .def("revPanoramaMaps", &MoilCV::revPanoramaMaps)

        .def("revPanorama", &MoilCV::revPanorama);
    }
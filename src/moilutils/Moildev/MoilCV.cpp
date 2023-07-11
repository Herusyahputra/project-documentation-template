#include "MoilCV.hpp"

double CJ_ONE = cos(30/180*2*3.14) ;
double CJ_ZERO = sin(30/180*2*3.14) ; //0) ;
double my_global_alpha_range_vender = 110 ;

MoilCV::MoilCV(string &name,  double cswidth,double csheight, double Icx, double Icy,
            double Ratio, double ImWidth, double ImHeight, double calibRatio, double Para0, double Para1,
            double Para2, double Para3, double Para4, double Para5){
            camera_Name=name;
            camera_SensorWidth=cswidth;
            camera_SensorHeight=csheight;
            camera_iCx=Icx;
            camera_iCy=Icy;
            camera_ratio=Ratio;
            camera_imageWidth=ImWidth;
            camera_imageHeight=ImHeight;
            camera_calibrationRatio=calibRatio;
            camera_para0=Para0;
            camera_para1=Para1;
            camera_para2=Para2;
            camera_para3=Para3;
            camera_para4=Para4;
            camera_para5=Para5;
            initAlphaRho_Table();
            }

MoilCV::~MoilCV() {}

double MoilCV::AnyPointM(py::array_t<float> array, py::array_t<float> array_b, double alphaOffset, double betaOffset, double zoom) {
        auto buf = array.request();
        auto buf2 = array_b.request();
        int h = array.shape()[0], w = array.shape()[1];
        float* mapX = (float*) buf.ptr;
        float* mapY = (float*) buf2.ptr;

        double icx = camera_iCx * camera_ratio;
        double icy = camera_iCy * camera_ratio;
        double dcx = camera_imageWidth/2 * camera_ratio;
        double dcy = camera_imageHeight/2 * camera_ratio;

        betaOffset += 180;
        double mAlphaOffset = alphaOffset * (PI / 180);
        double mBetaOffset = betaOffset * (PI / 180);
        double senH, senV, tempX, tempY, tempZ, beta, alpha;

        double origPostionX, origPostionY;
        double widthCosB = PCT_UNIT_WIDTH * cos(mBetaOffset);
        double heightCosASinB = PCT_UNIT_HEIGHT * cos(mAlphaOffset) * sin(mBetaOffset);
        double flZoomSinASinB = FOCAL_LENGTH_FOR_ZOOM * zoom * sin(mAlphaOffset) * sin(mBetaOffset);
        double widthSinB = PCT_UNIT_WIDTH * sin(mBetaOffset);
        double heightCosACosB = PCT_UNIT_HEIGHT * cos(mAlphaOffset) * cos(mBetaOffset);
        double flZoomSinACosB = FOCAL_LENGTH_FOR_ZOOM * zoom * sin(mAlphaOffset) * cos(mBetaOffset);
        double heightSinA = PCT_UNIT_HEIGHT * sin(mAlphaOffset);
        double flZoomCosA = FOCAL_LENGTH_FOR_ZOOM * zoom * cos(mAlphaOffset);

        for (int positionY = 0; positionY < h; positionY++)
        {
            for (int positionX = 0; positionX < w; positionX++)
            {
                tempX = (positionX - dcx) * widthCosB - (positionY - dcy) * heightCosASinB + flZoomSinASinB;
                tempY = (positionX - dcx) * widthSinB + (positionY - dcy) * heightCosACosB - flZoomSinACosB;
                tempZ = (positionY - dcy) * heightSinA + flZoomCosA;

                alpha = atan2(sqrt(tempX * tempX + tempY * tempY), tempZ);
                // if (alpha <= 1.919862)
                {
                    if (tempX != 0)
                    {
                        beta = atan2(tempY, tempX);
                    }
                    else
                        if (tempY >= 0)
                            beta = PI / 2;
                        else
                            beta = -(PI / 2);

                    senH = icx * camera_SensorWidth * camera_ratio -
                            (
                                camera_para0 * alpha * alpha * alpha * alpha * alpha * alpha
                                + camera_para1 * alpha * alpha * alpha * alpha * alpha
                                + camera_para2 * alpha * alpha * alpha * alpha
                                + camera_para3 * alpha * alpha * alpha
                                + camera_para4 * alpha * alpha
                                + camera_para5 * alpha) * camera_calibrationRatio * camera_SensorHeight * camera_ratio
                            * cos(beta);

                    senV = icy * camera_SensorHeight -
                            (
                                 camera_para0 * alpha * alpha * alpha * alpha * alpha * alpha
                                + camera_para1 * alpha * alpha * alpha * alpha * alpha
                                + camera_para2 * alpha * alpha * alpha * alpha
                                + camera_para3 * alpha * alpha * alpha
                                + camera_para4 * alpha * alpha
                                + camera_para5 * alpha) * camera_calibrationRatio * camera_SensorHeight * camera_ratio
                            * sin(beta);

                    origPostionX = round(senH / (camera_SensorWidth *camera_ratio));
                    origPostionY = round(senV/ camera_SensorHeight);

                    if (origPostionX >= 0 && origPostionX < w && origPostionY >= 0 && origPostionY < h)
                    {
                        *(mapX + ( positionY * w + positionX )) = (float)origPostionX;
                        *(mapY + ( positionY * w + positionX )) = (float)origPostionY;
                    }
                    else
                    {
                        *(mapX + ( positionY * w + positionX )) = 0;
                        *(mapY + ( positionY * w + positionX )) = 0;
                    }
                }
            }
        }
        return 0;
    }


double MoilCV::AnyPointM2(py::array_t<float> array, py::array_t<float> array_b, double thetaX_degree, double thetaY_degree, double zoom){
        auto buf = array.request();
        auto buf2 = array_b.request();
        int h = array.shape()[0], w = array.shape()[1];
        float* mapX = (float*) buf.ptr;
        float* mapY = (float*) buf2.ptr;

        double icx = camera_iCx * camera_ratio;
        double icy = camera_iCy * camera_ratio;
        double dcx = camera_imageWidth/2 * camera_ratio;
        double dcy = camera_imageHeight/2 * camera_ratio;

        // betaOffset += 180;
        double thetaX = thetaX_degree * (PI / 180);
        double thetaY = thetaY_degree * (PI / 180);
        double senH, senV, tempX, tempY, tempZ, beta, alpha;
        double origPostionX, origPostionY;

        double widthCosB = PCT_UNIT_WIDTH * cos(thetaY);
        double heightSinASinB = PCT_UNIT_HEIGHT * sin(thetaX) * sin(thetaY);
        double flZoomCosASinB = FOCAL_LENGTH_FOR_ZOOM * zoom * cos(thetaX) * sin(thetaY);
        double heightCosA = PCT_UNIT_HEIGHT * cos(thetaX);
        double flZoomSinA = FOCAL_LENGTH_FOR_ZOOM * zoom * sin(thetaX);
        double widthSinB = PCT_UNIT_WIDTH * sin(thetaY);
        double heightSinACosB = PCT_UNIT_HEIGHT * sin(thetaX) * cos(thetaY);
        double flZoomCosACosB = FOCAL_LENGTH_FOR_ZOOM * zoom * cos(thetaX) * cos(thetaY);
        for (int positionY = 0; positionY < h; positionY++)
        {
            for (int positionX = 0; positionX < w; positionX++)
            {
                tempX = (positionX - dcx) * widthCosB + (positionY - dcy) * heightSinASinB + flZoomCosASinB;
                tempY = (positionY - dcy) * heightCosA - flZoomSinA;
                tempZ = -(positionX - dcx) * widthSinB + (positionY - dcy) * heightSinACosB + flZoomCosACosB;

                tempX = -tempX;
                tempY = -tempY;
                alpha = atan2(sqrt(tempX * tempX + tempY * tempY), tempZ);
                // if (alpha <= 1.919862)
                {
                    if (tempX != 0)
                        beta = atan2(tempY, tempX);
                    else if (tempY >= 0)
                        beta = PI / 2;
                    else
                        beta = -(PI / 2);

                    senH = icx * camera_SensorWidth * camera_ratio -
                           (
                               camera_para0 * alpha * alpha * alpha * alpha * alpha * alpha
                               + camera_para1 * alpha * alpha * alpha * alpha * alpha
                               + camera_para2 * alpha * alpha * alpha * alpha
                               + camera_para3 * alpha * alpha * alpha
                               + camera_para4 * alpha * alpha
                               + camera_para5 * alpha) * camera_calibrationRatio * camera_SensorHeight * camera_ratio
                           * cos(beta);

                    senV = icy * camera_SensorHeight -
                           (
                               camera_para0 * alpha * alpha * alpha * alpha * alpha * alpha
                               + camera_para1 * alpha * alpha * alpha * alpha * alpha
                               + camera_para2 * alpha * alpha * alpha * alpha
                               + camera_para3 * alpha * alpha * alpha
                               + camera_para4 * alpha * alpha
                               + camera_para5 * alpha) * camera_calibrationRatio * camera_SensorHeight * camera_ratio
                           * sin(beta);

                    origPostionX = round(senH / (camera_SensorWidth * camera_ratio));
                    origPostionY = round(senV / camera_SensorHeight);

                    if (origPostionX >= 0 && origPostionX < w && origPostionY >= 0 && origPostionY < h)
                    {
                        *(mapX + ( positionY * w + positionX )) = (float)origPostionX;
                        *(mapY + ( positionY * w + positionX )) = (float)origPostionY;
                    }
                    else
                    {
                        *(mapX + ( positionY * w + positionX )) = 0;
                        *(mapY + ( positionY * w + positionX )) = 0;
                    }
                }
            }
        }
    return 0;
    }

// begin here for car =======================================================
double MoilCV::xPanoramaM_Rt(py::array_t<float> array, py::array_t<float> array_b,
                                double my_p_alpha_max_vendor,
                                double p_iC_alpha_degree, double p_iC_beta_degree,
                                double p_alpha_from, double p_alpha_end)
{
    auto buf = array.request();
    auto buf2 = array_b.request();
    int p_rows = array.shape()[0], p_cols = array.shape()[1];
    float* mapX = (float*) buf.ptr;
    float* mapY = (float*) buf2.ptr;

    double icx = camera_iCx * camera_ratio;
    double icy = camera_iCy * camera_ratio;

    //const int a_p_rows = p_rows;
    //const int a_p_cols = p_cols;
    double origPostionX, origPostionY;
    int mem_offset = 0;
    double iC_alpha_pivot = p_iC_alpha_degree * PI / 180;
    double iC_beta_pivot = -p_iC_beta_degree * PI / 180;
    // iC_beta_pivot = PI/2 - iC_beta_pivot;

    //rotation axis K
    const double kx = sin(iC_alpha_pivot) * cos(iC_beta_pivot) ;
    const double ky = sin(iC_alpha_pivot) * sin(iC_beta_pivot) ;
    const double kz = cos(iC_alpha_pivot) ;

   //08042022
    double max_ing_alpha = 0;
    double min_ing_alpha = 3.14 ;
    double max_fish_alpha = 0;
    double min_fish_alpha = 3.14 ;

//    double alpha_unit = (p_alpha_end - p_alpha_from) / p_rows ;
    //for (int cur_row = 0; cur_row < p_rows; cur_row++)
    for (int cur_row = p_alpha_from * p_rows; cur_row < p_alpha_end * p_rows; cur_row++)
    //from 0.5*1440<720> to 1440*1.5<2160>
    {
        // change heree
        double ing_alpha ;
        //ing_alpha = (cur_row * alpha_unit + p_alpha_from) * my_global_alpha_range_vender * PI /180.0;
        ing_alpha = (double)cur_row / (double)p_rows * my_p_alpha_max_vendor * PI / 180;
        // ing_alpha 0.5*92.5*3.14/180

        const double target_alpha = iC_alpha_pivot + ing_alpha;
        double const Vx = sin(target_alpha) * cos(iC_beta_pivot);
        const double Vy = sin(target_alpha) * sin(iC_beta_pivot);
        const double az = cos(target_alpha);

        const double kxa_x = ky * az - kz * Vy;
        const double kxa_y = kz * Vx - kx * az;
        const double kxa_z = kx * Vy - ky * Vx;
        const double k_a = kx * Vx + ky * Vy + kz * az;

        for (int cur_col = 0; cur_col < p_cols; cur_col++)
        {
            // 0 <= <cur_beta> < 2*PI
            double  ing_beta;
            ing_beta = (double)cur_col / (double)p_cols * 2 * PI;
            double ing_sin_beta = sin(ing_beta);
            double ing_cos_beta = cos(ing_beta);
            double V_rot_x = ing_cos_beta * Vx + kxa_x * ing_sin_beta + kx * k_a * (1 - ing_cos_beta);
            double V_rot_y = ing_cos_beta * Vy + kxa_y * ing_sin_beta + ky * k_a * (1 - ing_cos_beta);
            double V_rot_z = ing_cos_beta * az + kxa_z * ing_sin_beta + kz * k_a * (1 - ing_cos_beta);

            double fish_alpha, fish_beta;
            fish_beta = atan2(V_rot_y, V_rot_x);
            fish_alpha = atan2(sqrt(pow(V_rot_x, 2) + pow(V_rot_y, 2)), V_rot_z);
            fish_beta = PI / 2 - fish_beta;

            //double alpha2vghIH = alpha_ih_vga(alpha);

            origPostionX = 1.0 * round(icx - alpha_ih_vga(fish_alpha) * camera_calibrationRatio * camera_ratio *cos(fish_beta));
            origPostionY = 1.0 * round(icy - alpha_ih_vga(fish_alpha) * camera_calibrationRatio * camera_ratio *sin(fish_beta));

            if (origPostionX >= 0 && origPostionX < p_cols && origPostionY >= 0 && origPostionY < p_rows) // && fish_alpha < my_global_alpha_range_vender /180 * PI)
            {
                *(mapX + (mem_offset)) = (float)origPostionX;
                *(mapY + (mem_offset++)) = (float)origPostionY;

                max_ing_alpha = max_ing_alpha < ing_alpha ? ing_alpha : max_ing_alpha ;
                min_ing_alpha = min_ing_alpha < ing_alpha ? min_ing_alpha : ing_alpha ;

                max_fish_alpha = max_fish_alpha < fish_alpha ? fish_alpha : max_fish_alpha ;
                min_fish_alpha = min_fish_alpha < fish_alpha ? min_fish_alpha : fish_alpha ;
            }
            else
            {
                *(mapX + (mem_offset)) = 0;
                *(mapY + (mem_offset++)) = 0;
            }
        }
    }
//    cout << endl <<endl ;
//    cout <<"max_ing_alpha: " << max_ing_alpha << endl ;
//    cout <<"min_ing_alpha: " << min_ing_alpha << endl ;
//
//    cout <<"max_fish_alpha: " << max_fish_alpha << endl ;
//    cout <<"min_fish_alpha: " << min_fish_alpha << endl << endl;
//    cout <<" my_global_alpha_range_vender: " << my_global_alpha_range_vender << endl << endl;

    return 0;
}

void (*fun_euler_rotate)(const double c1, const double s1,
                      const double c2, const double s2,
                      const double c3, const double s3,
                      double uX, double uY, double uZ,
                      double &tempX, double &tempY, double &tempZ);

static void euler_XYZ (const double c1, const double s1, const double c2, const double s2, const double c3,
                         const double s3, double uX, double uY, double uZ, double &tempX, double &tempY,
                         double &tempZ)
{
    tempX = uX * (c2*c3)            + uY* (-c2*s3)            + uZ* (s2) ;
    tempY = uX * (c1*s3+c3*s1*s2)   + uY* (c1*c3 - s1*s2*s3)  + uZ* (-c2*s1);
    tempZ = uX * (s1*s3-c1*c3*s2)   + uY* (c3*s1+c1*s2*s3)    + uZ* (c1*c2);
}

static void euler_z1x2z3(const double c1, const double s1, const double c2, const double s2, const double c3,
                         const double s3, double uX, double uY, double uZ, double &tempX, double &tempY,
                         double &tempZ)
{  //M1 only now 03-24-2022
    tempX = (c1 * c3 - c2 * s1 * s3) * uX + (-c1 * s3 - c2 * c3 * s1) * uY + (s1 * s2) * uZ;
    tempY = (c3 * s1 + c1 * c2 * s3) * uX + (c1 * c2 * c3 - s1 * s3) * uY + (-c1 * s2) * uZ;
    tempZ = (s2 * s3) * uX + (c3 * s2) * uY + (c2)*uZ;
}

static double get_mapped_alpha(double a_thita, double a_phi, double a_psi, int positionX, int positionY, int dcx, int dcy,
                               double my_PCT_UNIT_WIDTH,
                               double my_PCT_UNIT_HEIGHT,
                               double myFOCAL_LENGTH_FOR_ZOOM,
                               void (*p_fun_euler_rotate)(const double c1, const double s1, const double c2,
                                                          const double s2, const double c3,
                                                          const double s3, double uX, double uY, double uZ, double &tempX,
                                                          double &tempY,
                                                          double &tempZ))
{
    double c1 = cos(a_thita);
    double s1 = sin(a_thita);
    double c2 = cos(a_phi);
    double s2 = sin(a_phi);
    double c3 = cos(a_psi) ; //CJ_ONE;
    double s3 = sin(a_psi) ; //CJ_ZERO;
    double uX = (positionX - dcx) * my_PCT_UNIT_WIDTH;
    double uY = (positionY - dcy) * my_PCT_UNIT_HEIGHT;
    double uZ = myFOCAL_LENGTH_FOR_ZOOM;
    double X, Y, Z;
    p_fun_euler_rotate(c1, s1, c2, s2, c3, s3, uX, uY, uZ, X, Y, Z);
    X = -X;
    Y = -Y;
    double alpha = atan2(sqrt(X * X + Y * Y), Z);
//     cout << "fun_ptr_get_alpha(alpha): " << alpha << endl ;
    return alpha;
}

double MoilCV::CarAnyPoint(py::array_t<float> array, py::array_t<float> array_b,
                             double pch_azm_pivot,
                             double yaw_zth_pivot,
                             double cj_roll_degree,
                             double zoom_over)
{
    AnyPoint_M_M(array, array_b,
                 yaw_zth_pivot,
                 pch_azm_pivot,
                 cj_roll_degree,
                 zoom_over,
                 *euler_XYZ);
    return 0;
}

double MoilCV::NewAnyPointM(py::array_t<float> array, py::array_t<float> array_b,
                             double alphaOffset,
                             double betaOffset,
                             double zoom)
{
    AnyPoint_M_M(array, array_b,
                 alphaOffset,
                 betaOffset,
                 0.0,
                 zoom,
                 *euler_z1x2z3);
    return 0;
}


double MoilCV::AnyPoint_M_M(py::array_t<float> array, py::array_t<float> array_b,
                             double pch_azm_pivot,
                             double yaw_zth_pivot,
                             double cj_roll_degree,
                             double zoom_over,
                             void (*fun_euler_rotate)(const double c1, const double s1,
                                                      const double c2, const double s2,
                                                      const double c3, const double s3,
                                                      double uX, double uY, double uZ,
                                                      double &tempX, double &tempY, double &tempZ))
{
    auto buf = array.request();
    auto buf2 = array_b.request();
    int mapper_height = array.shape()[0], mapper_width = array.shape()[1];
    float* mapX = (float*) buf.ptr;
    float* mapY = (float*) buf2.ptr;

    double a_rcpr_zoom = 1.0 / zoom_over;
    double my_PCT_UNIT_WIDTH = 1.0;   //? <PCT phyical unit>
    double my_PCT_UNIT_HEIGHT = 1.0;
    double my_h_VIRTUAL_FOCAL_LENGTH_w_ZOOM = mapper_width / 2 * my_PCT_UNIT_WIDTH * a_rcpr_zoom;
    // default unit focal length is 60 degrees, i.e. cos(60 degree) is 1/2.
    // bool to_adjust_mapper_center = true;

    double my_ALPHA_IN_RADIA = my_global_alpha_range_vender  * PI / 180; ////////////////////
    int my_h_offset = 0 ;
    int my_v_offset = 0 ;
    double sensor_asp = camera_SensorHeight / camera_SensorWidth;
    const double icx = camera_iCx;
    const double icy = camera_iCy;
    double a_dcx = camera_imageWidth / 2 + my_h_offset; // center of mapper, here, as 2D mapper origin
    double a_dcy = camera_imageHeight / 2 + my_v_offset;

    const double a_pch_vir_axis_in_radian = pch_azm_pivot * (PI / 180); // Scale to rotate XYZ
    const double a_yaw_vir_axis_in_radian = yaw_zth_pivot * (PI / 180);
    const double a_roll_vir_axis_in_radian = cj_roll_degree * PI / 180;

    double right_most;
    double left_most;
    double top_most;
    double down_most;
    {
        left_most = get_mapped_alpha(a_yaw_vir_axis_in_radian, a_pch_vir_axis_in_radian, a_roll_vir_axis_in_radian,
                                     0, mapper_height / 2,
                                     mapper_width / 2, mapper_height / 2,
                                     my_PCT_UNIT_WIDTH, my_PCT_UNIT_HEIGHT, my_h_VIRTUAL_FOCAL_LENGTH_w_ZOOM,
                                     *fun_euler_rotate);
        right_most = get_mapped_alpha(a_yaw_vir_axis_in_radian, a_pch_vir_axis_in_radian, a_roll_vir_axis_in_radian,
                                      mapper_width, mapper_height / 2,
                                      mapper_width / 2, mapper_height / 2,
                                      my_PCT_UNIT_WIDTH, my_PCT_UNIT_HEIGHT, my_h_VIRTUAL_FOCAL_LENGTH_w_ZOOM,
                                      *fun_euler_rotate);

        top_most = get_mapped_alpha(a_yaw_vir_axis_in_radian, a_pch_vir_axis_in_radian, a_roll_vir_axis_in_radian,
                                    mapper_width / 2,
                                    0, // mapper-ceiling
                                    mapper_width / 2,
                                    mapper_height / 2,
                                    my_PCT_UNIT_WIDTH, my_PCT_UNIT_HEIGHT, my_h_VIRTUAL_FOCAL_LENGTH_w_ZOOM,
                                    *fun_euler_rotate);

        down_most = get_mapped_alpha(a_yaw_vir_axis_in_radian, a_pch_vir_axis_in_radian, a_roll_vir_axis_in_radian,
                                     mapper_width / 2,
                                     mapper_height, // mapper-bottom
                                     mapper_width / 2,
                                     mapper_height / 2,
                                     my_PCT_UNIT_WIDTH, my_PCT_UNIT_HEIGHT, my_h_VIRTUAL_FOCAL_LENGTH_w_ZOOM,
                                     *fun_euler_rotate);
    }
    if (right_most > my_ALPHA_IN_RADIA)
    {
        for (; a_dcx < mapper_width; a_dcx += 1)
        {

            right_most = get_mapped_alpha(a_yaw_vir_axis_in_radian, a_pch_vir_axis_in_radian, a_roll_vir_axis_in_radian,

                                          mapper_width, mapper_height / 2,
                                          a_dcx,
                                          mapper_height / 2,
                                          my_PCT_UNIT_WIDTH, my_PCT_UNIT_HEIGHT, my_h_VIRTUAL_FOCAL_LENGTH_w_ZOOM,
                                          *fun_euler_rotate);

            if (right_most < my_ALPHA_IN_RADIA)
            {
                break;
            }
        }
    }
    else if (left_most > my_ALPHA_IN_RADIA)
    {

        for (; a_dcx > 0; a_dcx -= 1)
        {

            left_most = get_mapped_alpha(a_yaw_vir_axis_in_radian, a_pch_vir_axis_in_radian, a_roll_vir_axis_in_radian,
                                         0,
                                         mapper_height / 2,
                                         mapper_width / 2,
                                         mapper_height / 2,
                                         my_PCT_UNIT_WIDTH, my_PCT_UNIT_HEIGHT, my_h_VIRTUAL_FOCAL_LENGTH_w_ZOOM,
                                         *fun_euler_rotate);

            if (left_most < my_ALPHA_IN_RADIA)
            {
                break;
            }
        }
    }

    if (down_most > my_ALPHA_IN_RADIA)
    {
        for (; a_dcy < mapper_height; a_dcy += 1)
        {
            down_most = get_mapped_alpha(a_yaw_vir_axis_in_radian, a_pch_vir_axis_in_radian, a_roll_vir_axis_in_radian,
                                         mapper_width / 2,
                                         mapper_height, ///// mapper-floor
                                         mapper_width / 2,
                                         a_dcy,
                                         my_PCT_UNIT_WIDTH, my_PCT_UNIT_HEIGHT, my_h_VIRTUAL_FOCAL_LENGTH_w_ZOOM,
                                         *fun_euler_rotate);
            if (down_most < my_ALPHA_IN_RADIA)
            {
                break;
            }
        }
    }

    else if (top_most > my_ALPHA_IN_RADIA)
    {
        for (; a_dcy > 0; a_dcy -= 1)
        {
            top_most = get_mapped_alpha(a_yaw_vir_axis_in_radian, a_pch_vir_axis_in_radian, a_roll_vir_axis_in_radian,

                                        mapper_width / 2,
                                        0, /////mapper-ceiling
                                        mapper_width / 2,
                                        a_dcy,
                                        my_PCT_UNIT_WIDTH, my_PCT_UNIT_HEIGHT, my_h_VIRTUAL_FOCAL_LENGTH_w_ZOOM,
                                        *fun_euler_rotate);
            if (top_most < my_ALPHA_IN_RADIA)
            {
                break;
            }
        }
    }

    double alpha_max = 0.0;
    double beta, alpha;

    const double c1 = cos(a_yaw_vir_axis_in_radian);
    const double s1 = sin(a_yaw_vir_axis_in_radian);
    const double c2 = cos(a_pch_vir_axis_in_radian);
    const double s2 = sin(a_pch_vir_axis_in_radian);
    const double c3 = cos(a_roll_vir_axis_in_radian);
    const double s3 = sin(a_roll_vir_axis_in_radian);
    int aTmp = 0;

    // a_dcx = a_dcx + mapper_width - orig_x ;
    for (int positionY = 0; positionY < mapper_height; positionY++)
    {
        for (int positionX = aTmp; positionX < mapper_width + aTmp; positionX++)
        {
            double vx = (positionX - a_dcx) * my_PCT_UNIT_WIDTH;
            double vy = (positionY - a_dcy) * my_PCT_UNIT_HEIGHT;

            double uX = vx;
            double uY = vy;
            double uZ = my_h_VIRTUAL_FOCAL_LENGTH_w_ZOOM;

            double tempX;
            double tempY;
            double tempZ;
            fun_euler_rotate(c1, s1, c2, s2, c3, s3, uX, uY, uZ, tempX, tempY, tempZ);

            alpha = atan2(sqrt(tempX * tempX + tempY * tempY), tempZ);

            tempX = -tempX;
            tempY = -tempY;
            if (alpha <= my_ALPHA_IN_RADIA) // * PI / 180) // 110 degree, max alpha of raspPI
            {
                alpha_max = (alpha_max > alpha) ? alpha_max : alpha;
                if (tempX != 0)
                    beta = atan2(tempY, tempX);
                else if (tempY >= 0)
                    beta = PI / 2;
                else
                    beta = -(PI / 2);

                double vga_ih = alpha_ih_vga(alpha);

                double opt_h = icx * camera_SensorWidth - // * sensor_asp -
                               vga_ih * camera_calibrationRatio // un-normalize VGA
                                   * camera_SensorWidth / sensor_asp * cos(beta);
                double orig_x = round(opt_h / camera_SensorWidth);

                double opt_v = icy * camera_SensorHeight -
                               vga_ih * camera_calibrationRatio * camera_SensorHeight * sin(beta);
                double orig_y = round(opt_v / camera_SensorHeight);

                if (orig_x >= 0 && orig_x < mapper_width && orig_y >= 0 && orig_y < mapper_height)
                {
                    *(mapX + (positionY * mapper_width + positionX)) = (float)orig_x;
                    *(mapY + (positionY * mapper_width + positionX)) = (float)orig_y;
                }
                else
                {
                    *(mapX + (positionY * mapper_width + positionX)) = 0;
                    *(mapY + (positionY * mapper_width + positionX)) = 0;
                }
            }
        }
    }
    return 0;
}

double MoilCV::alpha_ih_vga(double p_alpha_in_rad) const
{
    return (camera_para0 * p_alpha_in_rad * p_alpha_in_rad * p_alpha_in_rad * p_alpha_in_rad * p_alpha_in_rad *
                p_alpha_in_rad +
            camera_para1 * p_alpha_in_rad * p_alpha_in_rad * p_alpha_in_rad * p_alpha_in_rad * p_alpha_in_rad +
            camera_para2 * p_alpha_in_rad * p_alpha_in_rad * p_alpha_in_rad * p_alpha_in_rad +
            camera_para3 * p_alpha_in_rad * p_alpha_in_rad * p_alpha_in_rad +
            camera_para4 * p_alpha_in_rad * p_alpha_in_rad +
            camera_para5 * p_alpha_in_rad);
}

//void MoilCV::fish_rotate(py::array_t<uint8_t> src, py::array_t<uint8_t> dst, double degree) {
//    auto Image = src.mutable_unchecked<3>();
//    auto result = dst.mutable_unchecked<3>();
//
//    int rows = Image.shape(0);
//    int cols = Image.shape(1);
//    double rads = degree *3.1416/180.0 ;
//    cout << endl << "void Moildev::fish_rotate()+++" << endl ;
//    for (int r=0;r<rows;r++)
//	{
//		for(int l=0;l<cols;l++)
//		{
//            int r1, c1;
//            r1=(int)(r0+((r-camera_iCy)*cos(rads))-((l-camera_iCx)*sin(rads)));
//			c1=(int)(camera_iCx+((r-camera_iCy)*sin(rads))+((l-camera_iCx)*cos(rads)));
//			if(r1>=0 && r1 < rows && c1 >=0 && c1 << cols){
//                for(int chn=0; chn<3; chn++)
////                result(r, l,chn) = Image(origPostionY, origPostionX,k);
//                 *(result+ (r1 * cols + c1)*3+chn) = *(Image + (r*cols + l)*3+chn) ;
//            }
//		}
//	}
//}

// here finish =============================================


double MoilCV::alpha2IH(double p_alpha_in_rad)
{
    return (camera_para0 * p_alpha_in_rad * p_alpha_in_rad * p_alpha_in_rad * p_alpha_in_rad * p_alpha_in_rad * p_alpha_in_rad +
            camera_para1 * p_alpha_in_rad * p_alpha_in_rad * p_alpha_in_rad * p_alpha_in_rad * p_alpha_in_rad +
            camera_para2 * p_alpha_in_rad * p_alpha_in_rad * p_alpha_in_rad * p_alpha_in_rad +
            camera_para3 * p_alpha_in_rad * p_alpha_in_rad * p_alpha_in_rad +
            camera_para4 * p_alpha_in_rad * p_alpha_in_rad +
            camera_para5 * p_alpha_in_rad);
}

double MoilCV::PanoramaX(py::array_t<float> array, py::array_t<float> array_b, double alpha_min, double alpha_max){
    auto buf = array.request();
    auto buf2 = array_b.request();
    int h = array.shape()[0], w = array.shape()[1];
    float* mapX = (float*) buf.ptr;
    float* mapY = (float*) buf2.ptr;

    double a_icx = camera_iCx * camera_ratio;
    double a_icy = camera_iCy * camera_ratio;
    double a_alpha, a_beta;
    int a_max_row_seq = h;
    int a_max_col_seq = w;
    double a_srcPostionX, a_srcPostionY;
    int a_mem_inc = 0;
    const double D2R = 2.0 * PI / 360.0;
    const double R2D = 360.0 / 2.0 / PI;
    double brickH ;
    double a_zone ;
        {
            static bool a_first = true;
            if (a_first)
            {
                int dst_height = h;
                dst_height = h ;

                double alpha_bound[2] = {alpha_min, alpha_max};  //--------modify here---------
                assert(alpha_bound[0] >= 1.0); //limit

                double h_bound[2] = {90 - alpha_bound[0], 90 - alpha_bound[1]}; //{65, -20} ;
                assert(h_bound[0] > h_bound[1]);

                double zone[2];
                for (unsigned int i = 0; i < 2; i++)
                    {
                        zone[i] = tan(h_bound[i] * D2R);
                    }
                double zone_length = zone[0] - zone[1];
                brickH = zone_length / dst_height;
                a_zone = zone[0] ;
            }
        }

        for (int a_positionY = 0; a_positionY < a_max_row_seq; a_positionY++) //PanoH
        {
            a_alpha = (90.0 - atan(a_zone - brickH * a_positionY) * R2D);
            double alpha_cal = alpha2IH(a_alpha * D2R) ;

            for (int a_positionX = 0; a_positionX < a_max_col_seq; a_positionX++)
            {
                a_beta = (double)a_positionX / (double)a_max_col_seq * 2 * PI;
                a_beta = PI / 2 - a_beta;

                a_srcPostionX = round(a_icx - alpha_cal * camera_calibrationRatio * camera_ratio * cos(a_beta)); // aspek ratio here must modify
                a_srcPostionY = round(a_icy - alpha_cal * camera_calibrationRatio * camera_ratio * sin(a_beta));
                if (a_srcPostionX >= 0 && a_srcPostionX < a_max_col_seq && a_srcPostionY >= 0 && a_srcPostionY < a_max_row_seq)
                {
                    *(mapX + (a_mem_inc)) = (float)a_srcPostionX;
                    *(mapY + (a_mem_inc++)) = (float)a_srcPostionY;
                }
                else
                {
                    *(mapX + (a_mem_inc)) = 0;
                    *(mapY + (a_mem_inc++)) = 0;
                }
            }
        }
        return 0;
    }

double MoilCV::PanoramaM_Rt(py::array_t<float> array, py::array_t<float> array_b, double alpha_max, double iC_alpha_degree, double iC_beta_degree){
    auto buf = array.request();
    auto buf2 = array_b.request();
    int h = array.shape()[0], w = array.shape()[1];
    float* mapX = (float*) buf.ptr;
    float* mapY = (float*) buf2.ptr;

    double icx = camera_iCx * camera_ratio;
    double icy = camera_iCy * camera_ratio;
    double alpha_inc, beta_inc;
    double alpha, beta;
    int rows = h;
    int cols = w;
    double origPostionX, origPostionY;
    int mem_inc = 0;
    double iC_alpha = iC_alpha_degree * PI / 180;
    double iC_beta = - iC_beta_degree * PI / 180;

    for (int positionY = 0; positionY < rows; positionY++)
    {
        alpha_inc = (double)positionY / (double)rows * alpha_max * PI / 180;

        for (int positionX = 0; positionX < cols; positionX++)
        {
            beta_inc = (double)positionX / (double)cols * 2 * PI;

            double a_alpha = iC_alpha+alpha_inc ;
            double ax = sin(a_alpha)*cos(iC_beta);
            double ay = sin(a_alpha)*sin(iC_beta);
            double az = cos(a_alpha);
            double kx = sin(iC_alpha)*cos(iC_beta);
            double ky = sin(iC_alpha)*sin(iC_beta);
            double kz = cos(iC_alpha);
            double sin_beta_inc = sin(beta_inc);
            double cos_beta_inc = cos(beta_inc);
            double kxa_x = ky * az - kz * ay;
            double kxa_y = kz * ax - kx * az;
            double kxa_z = kx * ay - ky * ax;
            double k_a = kx * ax + ky * ay + kz * az;

            double bx = cos_beta_inc * ax + kxa_x * sin_beta_inc + kx * k_a * ( 1 - cos_beta_inc );
            double by = cos_beta_inc * ay + kxa_y * sin_beta_inc + ky * k_a * ( 1 - cos_beta_inc );
            double bz = cos_beta_inc * az + kxa_z * sin_beta_inc + kz * k_a * ( 1 - cos_beta_inc );
            beta = atan2(by,bx);
            alpha = atan2( sqrt(pow(bx,2)+pow(by,2)), bz);

            beta = PI/2  - beta;

            double alpha_cal = (
                                   camera_para0 * alpha * alpha * alpha * alpha * alpha * alpha
                                   + camera_para1 * alpha * alpha * alpha * alpha * alpha
                                   + camera_para2 * alpha * alpha * alpha * alpha
                                   + camera_para3 * alpha * alpha * alpha
                                   + camera_para4 * alpha * alpha
                                   + camera_para5 * alpha );

            origPostionX = round( icx - alpha_cal * camera_calibrationRatio * camera_ratio * cos(beta) );
            origPostionY = round( icy - alpha_cal * camera_calibrationRatio * camera_ratio * sin(beta) );
            if (origPostionX >= 0 && origPostionX < cols && origPostionY >= 0 && origPostionY < rows)
            {
                *(mapX + ( mem_inc )) = (float)origPostionX;
                *(mapY + ( mem_inc++ )) = (float)origPostionY;
            }
            else
            {
                *(mapX + ( mem_inc )) = 0;
                *(mapY + ( mem_inc++ )) = 0;
            }
        }
    }
    return 0;
}

// created by anto: make a function that can return the anypoint using manually remapping
// the performance was not very good
double MoilCV::anypointImageModeM(py::array_t<uint8_t> src, py::array_t<uint8_t> dst,
                                  double alphaOffset,
                                  double betaOffset,
                                  double zoom){
    auto Image = src.mutable_unchecked<3>();
    auto result = dst.mutable_unchecked<3>();

    int h = Image.shape(0);
    int w = Image.shape(1);
    int c = Image.shape(2);

    double icx = camera_iCx * camera_ratio;
    double icy = camera_iCy * camera_ratio;
    double dcx = camera_imageWidth/2 * camera_ratio;
    double dcy = camera_imageHeight/2 * camera_ratio;

    betaOffset += 180;
    double mAlphaOffset = alphaOffset * (PI / 180);
    double mBetaOffset = betaOffset * (PI / 180);
    double senH, senV, tempX, tempY, tempZ, beta, alpha;

    double origPostionX, origPostionY;
    double widthCosB = PCT_UNIT_WIDTH * cos(mBetaOffset);
    double heightCosASinB = PCT_UNIT_HEIGHT * cos(mAlphaOffset) * sin(mBetaOffset);
    double flZoomSinASinB = FOCAL_LENGTH_FOR_ZOOM * zoom * sin(mAlphaOffset) * sin(mBetaOffset);
    double widthSinB = PCT_UNIT_WIDTH * sin(mBetaOffset);
    double heightCosACosB = PCT_UNIT_HEIGHT * cos(mAlphaOffset) * cos(mBetaOffset);
    double flZoomSinACosB = FOCAL_LENGTH_FOR_ZOOM * zoom * sin(mAlphaOffset) * cos(mBetaOffset);
    double heightSinA = PCT_UNIT_HEIGHT * sin(mAlphaOffset);
    double flZoomCosA = FOCAL_LENGTH_FOR_ZOOM * zoom * cos(mAlphaOffset);
    for (int positionY = 0; positionY < h ; positionY++){
        for (int positionX = 0; positionX < w ; positionX++){
            for (int k = 0; k < c; k++){
                tempX = (positionX - dcx) * widthCosB - (positionY - dcy) * heightCosASinB + flZoomSinASinB;
                tempY = (positionX - dcx) * widthSinB + (positionY - dcy) * heightCosACosB - flZoomSinACosB;
                tempZ = (positionY - dcy) * heightSinA + flZoomCosA;

                alpha = atan2(sqrt(tempX * tempX + tempY * tempY), tempZ);
                // if (alpha <= 1.919862)
                {
                    if (tempX != 0)
                    {
                        beta = atan2(tempY, tempX);
                    }
                    else
                        if (tempY >= 0)
                            beta = PI / 2;
                        else
                            beta = -(PI / 2);

                    senH = icx * camera_SensorWidth * camera_ratio -
                            (
                                camera_para0 * alpha * alpha * alpha * alpha * alpha * alpha
                                + camera_para1 * alpha * alpha * alpha * alpha * alpha
                                + camera_para2 * alpha * alpha * alpha * alpha
                                + camera_para3 * alpha * alpha * alpha
                                + camera_para4 * alpha * alpha
                                + camera_para5 * alpha) * camera_calibrationRatio * camera_SensorHeight * camera_ratio
                            * cos(beta);

                    senV = icy * camera_SensorHeight -
                            (
                                 camera_para0 * alpha * alpha * alpha * alpha * alpha * alpha
                                + camera_para1 * alpha * alpha * alpha * alpha * alpha
                                + camera_para2 * alpha * alpha * alpha * alpha
                                + camera_para3 * alpha * alpha * alpha
                                + camera_para4 * alpha * alpha
                                + camera_para5 * alpha) * camera_calibrationRatio * camera_SensorHeight * camera_ratio
                            * sin(beta);

                    origPostionX = round(senH / (camera_SensorWidth *camera_ratio));
                    origPostionY = round(senV/ camera_SensorHeight);

                    if (origPostionX >= 0 && origPostionX < w && origPostionY >= 0 && origPostionY < h)
                        {
                            result(positionY, positionX,k) = Image(origPostionY, origPostionX,k);
                        }
                    else
                        {
                            result(positionY, positionX, k) = 0;
                        }
                    }
                }
            }
    }
    return 0;
}

// created by anto: create maps for re-centering/change the optical point of the fisheye image. this function will return the maps
// here is create maps for reverse image, speed the computation more than 30%
double MoilCV::revPanoramaMaps(py::array_t<float> array, py::array_t<float> array_b, double alpha_max, double beta_offset){
    // modiffy by anto 05132022..
    auto buf = array.request();
    auto buf2 = array_b.request();
    int h = array.shape()[0], w = array.shape()[1];
    float* mapX = (float*) buf.ptr;
    float* mapY = (float*) buf2.ptr;

    double icx = camera_iCx;
    double icy = camera_iCy;
    double alpha, beta;
    int mem_inc = 0;

    double origPostionX, origPostionY;
    for (int i = 0; i < h ; i++){
        for (int j = 0; j < w ; j++){
            double r = sqrt(pow(j - icx, 2)+pow(i - icy, 2));
            alpha = getAlphaFromRho((int)r);
            beta = atan2(icy-i, j-icx) - (PI/2);
            beta += beta_offset * PI / 180;
            while( beta < 0 ) beta+= PI*2;

            origPostionX = round( camera_imageWidth * beta / (PI*2));
            origPostionY = round( camera_imageHeight * alpha / alpha_max );

            if (origPostionX >= 0 && origPostionX < w && origPostionY >= 0 && origPostionY < h){
                *(mapX + (mem_inc )) = (float)origPostionX;
                *(mapY + (mem_inc ++)) = (float)origPostionY;
                }
            else{
                *(mapX + (mem_inc )) = 255;
                *(mapY + ( mem_inc++)) = 255;
                }
            }
        }
    return 0;
    }

double MoilCV::revPanorama(py::array_t<uint8_t> array, py::array_t<uint8_t> array_b, double alpha_max, double beta_offset){
    // modiffy by anto 04082021..
    auto panoImage = array.mutable_unchecked<3>();
    auto result = array_b.mutable_unchecked<3>();

    double icx = camera_iCx;
    double icy = camera_iCy;
    double alpha, beta;
    int h = panoImage.shape(0);
    int w = panoImage.shape(1);
    int c = panoImage.shape(2);

    double origPostionX, origPostionY;
    for (int i = 0; i < h ; i++)
    {
        for (int j = 0; j < w ; j++)
           {
           for (int k = 0; k < c; k++)
                {
                double r = sqrt(pow(j - icx, 2)+pow(i - icy, 2));
                alpha = getAlphaFromRho((int)r);
                beta = atan2(icy-i, j-icx) - (PI/2);
                beta += beta_offset * PI / 180;
                while( beta < 0 ) beta+= PI*2;

                origPostionX = round( camera_imageWidth * beta / (PI*2));
                origPostionY = round( camera_imageHeight * alpha / alpha_max );

                if (origPostionX >= 0 && origPostionX < w && origPostionY >= 0 && origPostionY < h)
                    {
                        result(i, j,k) = panoImage(origPostionY, origPostionX,k);
                    }
                else
                    {
                        result(i, j, k) = 0;
                    }
             }
        }
    }
    return 0;
    }

void MoilCV :: initAlphaRho_Table(){
    double alpha ;
        for (int i=0;i<1800;i++) {
            alpha = (double)i/10*PI/180;
            alphaToRho_Table[i] =
                        ( camera_para0 * alpha * alpha * alpha * alpha * alpha * alpha
                        + camera_para1 * alpha * alpha * alpha * alpha * alpha
                        + camera_para2 * alpha * alpha * alpha * alpha
                        + camera_para3 * alpha * alpha * alpha
                        + camera_para4 * alpha * alpha
                        + camera_para5 * alpha ) * camera_calibrationRatio;
        }
        int i=0, index = 0;
        while(i<1800) {
            while(index<this->alphaToRho_Table[i]){
                rhoToAlpha_Table[index++] = i;
            }
            i++;
        }
        while(index<3600){
            rhoToAlpha_Table[index++] = i;
        }
    }

int MoilCV :: getRhoFromAlpha( double alpha ){
        return (alphaToRho_Table[(int)round(alpha*10)]);
    }

double MoilCV :: getAlphaFromRho( int rho ){
    if (rho>=0)
    return ((double)rhoToAlpha_Table[rho]/10);
    else
    return (-(double)rhoToAlpha_Table[-rho]/10);

    }
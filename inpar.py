# finish 4 different objects: corn5, robot216, canyon1, flask7

class Vrml(object):
    extension = ''
    write_mode = ''
    external_internal_texture_mode = 0
    inside_out_transform = 0

class Imgdata(object):
    tname = ''
    vrml = Vrml()

def buildImgData(tname, extension, workmode, klt_replace_tag, total_frames_in_sequence,
                 n_sector_frames, base_frame_index, n_features,
                 markersize_features, z_init_meters, pixel_width_meters,
                 klt_check_xy_limit_tag, features_xy_limits,
                 klt_feature_motion_tag, features_motion_limits,
                 mismatch_filter_tag, threshold_epip_error, write_mode,
                 external_internal_texture_mode, inside_out_transform):

    imgdata = Imgdata()

    imgdata.tname = tname
    imgdata.extension = extension
    imgdata.workmode = workmode
    imgdata.klt_replace_tag = klt_replace_tag
    imgdata.total_frames_in_sequence = total_frames_in_sequence
    imgdata.n_sector_frames = n_sector_frames
    imgdata.Tinit = n_sector_frames - 1
    imgdata.base_frame_index = base_frame_index
    imgdata.n_features = n_features
    imgdata.markersize_features = markersize_features
    imgdata.z_init_meters = z_init_meters
    imgdata.pixel_width_meters = pixel_width_meters
    imgdata.klt_check_xy_limit_tag = klt_check_xy_limit_tag
    imgdata.features_xy_limits = features_xy_limits
    imgdata.klt_feature_motion_tag = klt_feature_motion_tag
    imgdata.features_motion_limits = features_motion_limits
    imgdata.mismatch_filter_tag = mismatch_filter_tag
    imgdata.threshold_epip_error = threshold_epip_error

    imgdata.vrml.extension = extension
    imgdata.vrml.write_mode = write_mode
    imgdata.vrml.external_internal_texture_mode = external_internal_texture_mode
    imgdata.vrml.inside_out_transform = inside_out_transform
    

    return imgdata

#function to build data
def inpar(temp):
    if temp == 'corn5':
        return buildImgData('corn5', '.bmp', 'lowe', 0, 29, 10, 1, 300,
                              3, 0.33, 0.00000542, 1, [100, 500, 100, 420],
                              1, [0.5, 100, 0.5, 100], 1, 0.3, 'one', 0, 0)
    elif temp == 'robot216':
        return buildImgData('robot216', '.jpg', 'lowe', 1, 293, 15, 1,
                              1000, 3, 0.33, 0.00000542, 1, [250, 900, 180, 680],
                              1, [0.05, 100, 0.05, 100], 0, 0.3, 'one', 0, 0)
    elif temp == 'canyon1':
        return buildImgData('canyon1', '.jpg', 'lowe', 0, 15, 14, 1, 1000,
                            3, 3.3, 0.00000542, 1, [10, 600, 15, 400], 1,
                            [-0.5, 100, -0.5, 100], 0, 0.3, 'one', 0, 0)
    elif temp == 'flask7':
        return buildImgData('flask7', '.bmp', 'lowe', 0, 29, 20, 1, 300,
                            3, 0.33, 0.00000542, 1, [250, 420, 40, 440], 1,
                            [0.05, 100, 0.05, 100], 0, 0.3, 'one', 0, 0)
    else:
        print 'No such images'



# quant to nii/mhd/nrrd data format
file_path= 'quant_data/WLS010011P5T2\\3D_QUANT_loss_30Hz\\0025_conf.quant'
ct = sitk.ReadImage(file_path)
ct_array = sitk.GetArrayFromImage(ct)
ct_sitk = sitk.GetImageFromArray(ct_array)
ct_sitk.SetOrigin(ct.GetOrigin())
ct_sitk.SetSpacing(ct.GetSpacing())
ct_sitk.SetDirection(ct.GetDirection())
sitk.WriteImage(ct_sitk, 'test2.nii')  # mhd, nrrrd

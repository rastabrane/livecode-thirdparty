{
	'includes':
	[
		'../../common.gypi',
	],
	
	'targets':
	[
		{
			'target_name': 'libskia',
			'type': 'static_library',
			
			'include_dirs':
			[
				'include/config',
				'include/core',
				'include/device',
				'include/effects',
				'include/gpu',
				'include/images',
				'include/pathops',
				'include/pdf',
				'include/pipe',
				'include/ports',
				'include/svg',
				'include/text',
				'include/utils',
				'src/core',
				'src/device',
				'src/effects',
				'src/fonts',
				'src/gpu',
				'src/image',
				'src/images',
				'src/opts',
				'src/pathops',
				'src/pdf',
				'src/pipe',
				'src/ports',
				'src/sfnt',
				'src/svg',
				'src/text',
				'src/utils',
			],
			
			'sources':
			[
				'src/core/Sk64.cpp',
				'src/core/SkAAClip.cpp',
				'src/core/SkAdvancedTypefaceMetrics.cpp',
				'src/core/SkAlphaRuns.cpp',
				'src/core/SkAnnotation.cpp',
				'src/core/SkBBoxHierarchyRecord.cpp',
				'src/core/SkBBoxRecord.cpp',
				'src/core/SkBitmap_scroll.cpp',
				'src/core/SkBitmap.cpp',
				'src/core/SkBitmapDevice.cpp',
				'src/core/SkBitmapFilter.cpp',
				'src/core/SkBitmapHeap.cpp',
				'src/core/SkBitmapProcShader.cpp',
				'src/core/SkBitmapProcState.cpp',
				'src/core/SkBitmapProcState_matrixProcs.cpp',
				'src/core/SkBitmapScaler.cpp',
				'src/core/SkBlitMask_D32.cpp',
				'src/core/SkBlitRow_D16.cpp',
				'src/core/SkBlitRow_D32.cpp',
				'src/core/SkBlitter.cpp',
				'src/core/SkBlitter_A8.cpp',
				'src/core/SkBlitter_ARGB32.cpp',
				'src/core/SkBlitter_RGB16.cpp',
				'src/core/SkBlitter_Sprite.cpp',
				'src/core/SkBuffer.cpp',
				'src/core/SkCanvas.cpp',
				'src/core/SkChunkAlloc.cpp',
				'src/core/SkClipStack.cpp',
				'src/core/SkColor.cpp',
				'src/core/SkColorFilter.cpp',
				'src/core/SkColorTable.cpp',
				'src/core/SkComposeShader.cpp',
				'src/core/SkConfig8888.cpp',
				'src/core/SkConvolver.cpp',
				'src/core/SkCordic.cpp',
				'src/core/SkCubicClipper.cpp',
				'src/core/SkData.cpp',
				'src/core/SkDataTable.cpp',
				'src/core/SkDebug.cpp',
				'src/core/SkDeque.cpp',
				'src/core/SkDevice.cpp',
				'src/core/SkDeviceLooper.cpp',
				'src/core/SkDeviceProfile.cpp',
				'src/core/SkDither.cpp',
				'src/core/SkDraw.cpp',
				'src/core/SkDrawLooper.cpp',
				'src/core/SkEdge.cpp',
				'src/core/SkEdgeBuilder.cpp',
				'src/core/SkEdgeClipper.cpp',
				'src/core/SkError.cpp',
				'src/core/SkFilterProc.cpp',
				'src/core/SkFilterShader.cpp',
				'src/core/SkFlate.cpp',
				'src/core/SkFlattenable.cpp',
				'src/core/SkFlattenableBuffers.cpp',
				'src/core/SkFlattenableSerialization.cpp',
				'src/core/SkFloat.cpp',
				'src/core/SkFloatBits.cpp',
				'src/core/SkFontDescriptor.cpp',
				'src/core/SkFontHost.cpp',
				'src/core/SkFontStream.cpp',
				'src/core/SkGeometry.cpp',
				'src/core/SkGlyphCache.cpp',
				'src/core/SkGraphics.cpp',
				'src/core/SkImageFilter.cpp',
				'src/core/SkImageFilterUtils.cpp',
				'src/core/SkImageInfo.cpp',
				'src/core/SkInstCnt.cpp',
				'src/core/SkLineClipper.cpp',
				'src/core/SkMallocPixelRef.cpp',
				'src/core/SkMask.cpp',
				'src/core/SkMaskFilter.cpp',
				'src/core/SkMaskGamma.cpp',
				'src/core/SkMath.cpp',
				'src/core/SkMatrix.cpp',
				'src/core/SkMetaData.cpp',
				'src/core/SkMipMap.cpp',
				'src/core/SkOrderedReadBuffer.cpp',
				'src/core/SkOrderedWriteBuffer.cpp',
				'src/core/SkPackBits.cpp',
				'src/core/SkPaint.cpp',
				'src/core/SkPaintOptionsAndroid.cpp',
				'src/core/SkPaintPriv.cpp',
				'src/core/SkPath.cpp',
				'src/core/SkPathEffect.cpp',
				'src/core/SkPathHeap.cpp',
				'src/core/SkPathMeasure.cpp',
				'src/core/SkPathRef.cpp',
				'src/core/SkPicture.cpp',
				'src/core/SkPictureFlat.cpp',
				'src/core/SkPicturePlayback.cpp',
				'src/core/SkPictureRecord.cpp',
				'src/core/SkPictureStateTree.cpp',
				'src/core/SkPixelRef.cpp',
				'src/core/SkPoint.cpp',
				'src/core/SkProcSpriteBlitter.cpp',
				'src/core/SkPtrRecorder.cpp',
				'src/core/SkQuadClipper.cpp',
				'src/core/SkRasterClip.cpp',
				'src/core/SkRasterizer.cpp',
				'src/core/SkRect.cpp',
				'src/core/SkRefDict.cpp',
				'src/core/SkRegion.cpp',
				'src/core/SkRegion_path.cpp',
				'src/core/SkRegion_rects.cpp',
				'src/core/SkRRect.cpp',
				'src/core/SkRTree.cpp',
				'src/core/SkScalar.cpp',
				'src/core/SkScaledImageCache.cpp',
				'src/core/SkScalerContext.cpp',
				'src/core/SkScan.cpp',
				'src/core/SkScan_Antihair.cpp',
				'src/core/SkScan_AntiPath.cpp',
				'src/core/SkScan_Hairline.cpp',
				'src/core/SkScan_Path.cpp',
				'src/core/SkShader.cpp',
				'src/core/SkSpriteBlitter_ARGB32.cpp',
				'src/core/SkSpriteBlitter_RGB16.cpp',
				'src/core/SkStream.cpp',
				'src/core/SkString.cpp',
				'src/core/SkStringUtils.cpp',
				'src/core/SkStroke.cpp',
				'src/core/SkStrokeRec.cpp',
				'src/core/SkStrokerPriv.cpp',
				'src/core/SkTileGrid.cpp',
				'src/core/SkTileGridPicture.cpp',
				'src/core/SkTLS.cpp',
				'src/core/SkTSearch.cpp',
				'src/core/SkTypeface.cpp',
				'src/core/SkTypefaceCache.cpp',
				'src/core/SkUnPreMultiply.cpp',
				'src/core/SkUtils.cpp',
				'src/core/SkUtilsArm.cpp',
				'src/core/SkValidatingReadBuffer.cpp',
				'src/core/SkWriter32.cpp',
				'src/core/SkXfermode.cpp',
				
				'src/effects/SkBlurMask.h',
				'src/effects/SkEmbossMask.h',
				'src/effects/SkEmbossMask_Table.h',
				'src/effects/SkGpuBlurUtils.h',
				
				'src/effects/Sk1DPathEffect.cpp',
				'src/effects/Sk2DPathEffect.cpp',
				'src/effects/SkArithmeticMode.cpp',
				'src/effects/SkAvoidXfermode.cpp',
				'src/effects/SkBicubicImageFilter.cpp',
				'src/effects/SkBitmapSource.cpp',
				'src/effects/SkBlurDrawLooper.cpp',
				'src/effects/SkBlurImageFilter.cpp',
				'src/effects/SkBlurMask.cpp',
				'src/effects/SkBlurMaskFilter.cpp',
				'src/effects/SkColorFilterImageFilter.cpp',
				'src/effects/SkColorFilters.cpp',
				'src/effects/SkColorMatrix.cpp',
				'src/effects/SkColorMatrixFilter.cpp',
				'src/effects/SkComposeImageFilter.cpp',
				'src/effects/SkCornerPathEffect.cpp',
				'src/effects/SkDashPathEffect.cpp',
				'src/effects/SkDiscretePathEffect.cpp',
				'src/effects/SkDisplacementMapEffect.cpp',
				'src/effects/SkDropShadowImageFilter.cpp',
				'src/effects/SkEmbossMask.cpp',
				'src/effects/SkEmbossMaskFilter.cpp',
				'src/effects/SkGpuBlurUtils.cpp',
				'src/effects/SkKernel33MaskFilter.cpp',
				'src/effects/SkLayerDrawLooper.cpp',
				'src/effects/SkLayerRasterizer.cpp',
				'src/effects/SkLerpXfermode.cpp',
				'src/effects/SkLightingImageFilter.cpp',
				'src/effects/SkLumaColorFilter.cpp',
				'src/effects/SkMagnifierImageFilter.cpp',
				'src/effects/SkMatrixConvolutionImageFilter.cpp',
				'src/effects/SkMergeImageFilter.cpp',
				'src/effects/SkMorphologyImageFilter.cpp',
				'src/effects/SkOffsetImageFilter.cpp',
				'src/effects/SkPaintFlagsDrawFilter.cpp',
				'src/effects/SkPerlinNoiseShader.cpp',
				'src/effects/SkPictureImageFilter.cpp',
				'src/effects/SkPixelXorXfermode.cpp',
				'src/effects/SkPorterDuff.cpp',
				'src/effects/SkRectShaderImageFilter.cpp',
				'src/effects/SkStippleMaskFilter.cpp',
				'src/effects/SkTableColorFilter.cpp',
				'src/effects/SkTableMaskFilter.cpp',
				'src/effects/SkTestImageFilters.cpp',
				'src/effects/SkTileImageFilter.cpp',
				'src/effects/SkTransparentShader.cpp',
				'src/effects/SkXfermodeImageFilter.cpp',
				
				'src/effects/gradients/SkBitmapCache.h',
				'src/effects/gradients/SkClampRange.h',
				'src/effects/gradients/SkGradientShaderPriv.h',
				'src/effects/gradients/SkLinearGradient.h',
				'src/effects/gradients/SkRadialGradient.h',
				'src/effects/gradients/SkRadialGradient_Table.h',
				'src/effects/gradients/SkSweepGradient.h',
				'src/effects/gradients/SkTwoPointConicalGradient.h',
				'src/effects/gradients/SkTwoPointRadialGradient.h',
				
				'src/effects/gradients/SkBitmapCache.cpp',
				'src/effects/gradients/SkClampRange.cpp',
				'src/effects/gradients/SkGradientShader.cpp',
				'src/effects/gradients/SkLinearGradient.cpp',
				'src/effects/gradients/SkRadialGradient.cpp',
				'src/effects/gradients/SkSweepGradient.cpp',
				'src/effects/gradients/SkTwoPointConicalGradient.cpp',
				'src/effects/gradients/SkTwoPointRadialGradient.cpp',
				
				'src/image/SkImage_Base.h',
				'src/image/SkImagePriv.h',
				'src/image/SkSurface_Base.h',
				
				'src/image/SkImage.cpp',
				'src/image/SkImagePriv.cpp',
				'src/image/SkImage_Codec.cpp',
				'src/image/SkImage_Gpu.cpp',
				'src/image/SkImage_Picture.cpp',
				'src/image/SkImage_Raster.cpp',
				'src/image/SkSurface.cpp',
				'src/image/SkSurface_Gpu.cpp',
				'src/image/SkSurface_Picture.cpp',
				'src/image/SkSurface_Raster.cpp',
				
				#'src/images/bmpdecoderhelper.h',
				'src/images/transform_scanline.h',
				'src/images/SkDecodingImageGenerator.h',
				'src/images/SkImageRef_ashmem.h',
				'src/images/SkImageRefPool.h',
				'src/images/SkJpegUtility.h',
				'src/images/SkScaledBitmapSampler.h',
				'src/images/SkStreamHelpers.h',
				
				#'src/images/bmpdecoderhelper.cpp',
				'src/images/SkDecodingImageGenerator.cpp',
				'src/images/SkForceLinking.cpp',
				'src/images/SkImageDecoder.cpp',
				'src/images/SkImageDecoder_FactoryDefault.cpp',
				'src/images/SkImageDecoder_FactoryRegistrar.cpp',
				#'src/images/SkImageDecoder_libbmp.cpp',
				#'src/images/SkImageDecoder_libgif.cpp',
				#'src/images/SkImageDecoder_libico.cpp',
				#'src/images/SkImageDecoder_libjpeg.cpp',
				#'src/images/SkImageDecoder_libpng.cpp',
				#'src/images/SkImageDecoder_libwebp.cpp',
				#'src/images/SkImageDecoder_wbmp.cpp',
				'src/images/SkImageEncoder.cpp',
				'src/images/SkImageEncoder_argb.cpp',
				'src/images/SkImageEncoder_Factory.cpp',
				'src/images/SkImageRef.cpp',
				'src/images/SkImageRef_ashmem.cpp',
				'src/images/SkImageRef_GlobalPool.cpp',
				'src/images/SkImageRefPool.cpp',
				'src/images/SkImages.cpp',
				#'src/images/SkJpegUtility.cpp',
				#'src/images/SkMovie.cpp',
				#'src/images/SkMovie_gif.cpp',
				'src/images/SkPageFlipper.cpp',
				'src/images/SkScaledBitmapSampler.cpp',
				'src/images/SkStreamHelpers.cpp',
				
				'src/opts/SkBitmapFilter_opts_SSE2.h',
				'src/opts/SkBitmapProcState_filter_neon.h',
				'src/opts/SkBitmapProcState_matrix_clamp_neon.h',
				'src/opts/SkBitmapProcState_matrix_repeat_neon.h',
				'src/opts/SkBitmapProcState_opts_SSE2.h',
				'src/opts/SkBitmapProcState_opts_SSSE3.h',
				'src/opts/SkBlitMask_opts_arm_neon.h',
				'src/opts/SkBlitRect_opts_SSE2.h',
				'src/opts/SkBlitRow_opts_arm_neon.h',
				'src/opts/SkBlitRow_opts_SSE2.h',
				'src/opts/SkBlurImage_opts.h',
				'src/opts/SkBlurImage_opts_neon.h',
				'src/opts/SkBlurImage_opts_SSE2.h',
				'src/opts/SkCachePreload_arm.h',
				'src/opts/SkColor_opts_neon.h',
				'src/opts/SkMorphology_opts.h',
				'src/opts/SkMorphology_opts_neon.h',
				'src/opts/SkMorphology_opts_SSE2.h',
				'src/opts/SkUtils_opts_SSE2.h',
				'src/opts/SkXfermode_opts_arm_neon.h',
				
				'src/opts/morphology_opts_check_mac.cpp',
				'src/opts/opts_check_arm.cpp',
				'src/opts/opts_check_mac.cpp',
				'src/opts/opts_check_SSE2.cpp',
				'src/opts/SkBitmapFilter_opts_SSE2.cpp',
				'src/opts/SkBitmapProcState_arm_neon.cpp',
				'src/opts/SkBitmapProcState_matrixProcs_neon.cpp',
				'src/opts/SkBitmapProcState_opts_arm.cpp',
				'src/opts/SkBitmapProcState_opts_none.cpp',
				'src/opts/SkBitmapProcState_opts_SSE2.cpp',
				'src/opts/SkBitmapProcState_opts_SSSE3.cpp',
				'src/opts/SkBlitMask_opts_arm_neon.cpp',
				'src/opts/SkBlitMask_opts_arm.cpp',
				'src/opts/SkBlitMask_opts_none.cpp',
				'src/opts/SkBlitRect_opts_SSE2.cpp',
				'src/opts/SkBlitRow_opts_arm_neon.cpp',
				'src/opts/SkBlitRow_opts_arm.cpp',
				'src/opts/SkBlitRow_opts_none.cpp',
				'src/opts/SkBlitRow_opts_SSE2.cpp',
				'src/opts/SkBlurImage_opts_neon.cpp',
				'src/opts/SkBlurImage_opts_none.cpp',
				'src/opts/SkBlurImage_opts_SSE2.cpp',
				'src/opts/SkMorphology_opts_neon.cpp',
				'src/opts/SkMorphology_opts_none.cpp',
				'src/opts/SkMorphology_opts_SSE2.cpp',
				'src/opts/SkUtils_opts_none.cpp',
				'src/opts/SkUtils_opts_SSE2.cpp',
				'src/opts/SkXfermode_opts_arm_neon.cpp',
				'src/opts/SkXfermode_opts_arm.cpp',
				'src/opts/SkXfermode_opts_none.cpp',
				'src/opts/memset.arm.S',
				'src/opts/memset16_neon.S',
				'src/opts/memset32_neon.S',
				
				'src/pathops/SkAddIntersections.h',
				'src/pathops/SkDQuadImplicit.h',
				'src/pathops/SkIntersectionHelper.h',
				'src/pathops/SkIntersections.h',
				'src/pathops/SkLineParameters.h',
				'src/pathops/SkOpAngle.h',
				'src/pathops/SkOpContour.h',
				'src/pathops/SkOpEdgeBuilder.h',
				'src/pathops/SkOpSegment.h',
				'src/pathops/SkOpSpan.h',
				'src/pathops/SkPathOpsBounds.h',
				'src/pathops/SkPathOpsCommon.h',
				'src/pathops/SkPathOpsCubic.h',
				'src/pathops/SkPathOpsCurve.h',
				'src/pathops/SkPathOpsDebug.h',
				'src/pathops/SkPathOpsLine.h',
				'src/pathops/SkPathOpsPoint.h',
				'src/pathops/SkPathOpsQuad.h',
				'src/pathops/SkPathOpsRect.h',
				'src/pathops/SkPathOpsTriangle.h',
				'src/pathops/SkPathOpsTypes.h',
				'src/pathops/SkPathWriter.h',
				'src/pathops/SkQuarticRoot.h',
				'src/pathops/SkReduceOrder.h',
				
				'src/pathops/SkAddIntersections.cpp',
				'src/pathops/SkDCubicIntersection.cpp',
				'src/pathops/SkDCubicLineIntersection.cpp',
				'src/pathops/SkDCubicToQuads.cpp',
				'src/pathops/SkDLineIntersection.cpp',
				'src/pathops/SkDQuadImplicit.cpp',
				'src/pathops/SkDQuadIntersection.cpp',
				'src/pathops/SkDQuadLineIntersection.cpp',
				'src/pathops/SkIntersections.cpp',
				'src/pathops/SkOpAngle.cpp',
				'src/pathops/SkOpContour.cpp',
				'src/pathops/SkOpEdgeBuilder.cpp',
				'src/pathops/SkOpSegment.cpp',
				'src/pathops/SkPathOpsBounds.cpp',
				'src/pathops/SkPathOpsCommon.cpp',
				'src/pathops/SkPathOpsCubic.cpp',
				'src/pathops/SkPathOpsDebug.cpp',
				'src/pathops/SkPathOpsLine.cpp',
				'src/pathops/SkPathOpsOp.cpp',
				'src/pathops/SkPathOpsPoint.cpp',
				'src/pathops/SkPathOpsQuad.cpp',
				'src/pathops/SkPathOpsRect.cpp',
				'src/pathops/SkPathOpsSimplify.cpp',
				'src/pathops/SkPathOpsTriangle.cpp',
				'src/pathops/SkPathOpsTypes.cpp',
				'src/pathops/SkPathWriter.cpp',
				'src/pathops/SkQuarticRoot.cpp',
				'src/pathops/SkReduceOrder.cpp',
				
				'src/ports/SkAtomics_android.h',
				'src/ports/SkAtomics_none.h',
				'src/ports/SkAtomics_sync.h',
				'src/ports/SkAtomics_win.h',
				'src/ports/SkFontConfigParser_android.h',
				'src/ports/SkFontConfigTypeface.h',
				'src/ports/SkFontHost_FreeType_common.h',
				'src/ports/SkMutex_none.h',
				'src/ports/SkMutex_pthread.h',
				'src/ports/SkMutex_win.h',
				
				'src/ports/SkDebug_android.cpp',
				#'src/ports/SkDebug_nacl.cpp',
				'src/ports/SkDebug_stdio.cpp',
				'src/ports/SkDebug_win.cpp',
				#'src/ports/SkDiscardableMemory_ashmem.cpp',
				#'src/ports/SkDiscardableMemory_none.cpp',
				'src/ports/SkFontConfigInterface_android.cpp',
				#'src/ports/SkFontConfigInterface_direct.cpp',
				'src/ports/SkFontConfigParser_android.cpp',
				#'src/ports/SkFontHost_android.cpp',
				'src/ports/SkFontHost_fontconfig.cpp',
				#'src/ports/SkFontHost_FreeType.cpp',
				#'src/ports/SkFontHost_FreeType_common.cpp',
				#'src/ports/SkFontHost_linux.cpp',
				#'src/ports/SkFontHost_mac.cpp',
				'src/ports/SkFontHost_none.cpp',
				#'src/ports/SkFontHost_win_dw.cpp',
				#'src/ports/SkFontHost_win.cpp',
				#'src/ports/SkFontMgr_default_dw.cpp',
				#'src/ports/SkFontMgr_default_gdi.cpp',
				#'src/ports/SkGlobalInitialization_chromium.cpp',
				'src/ports/SkGlobalInitialization_default.cpp',
				#'src/ports/SkHarfBuzzFont.cpp',
				#'src/ports/SkImageDecoder_CG.cpp',
				#'src/ports/SkImageDecoder_empty.cpp',
				#'src/ports/SkImageDecoder_WIC.cpp',
				'src/ports/SkMemory_malloc.cpp',
				#'src/ports/SkMemory_mozalloc.cpp',
				'src/ports/SkOSFile_none.cpp',
				'src/ports/SkOSFile_posix.cpp',
				'src/ports/SkOSFile_stdio.cpp',
				#'src/ports/SkOSFile_win.cpp',
				#'src/ports/SkPurgeableMemoryBlock_android.cpp',
				#'src/ports/SkPurgeableMemoryBlock_mac.cpp',
				#'src/ports/SkPurgeableMemoryBlock_none.cpp',
				'src/ports/SkTime_Unix.cpp',
				'src/ports/SkTime_win.cpp',
				'src/ports/SkTLS_none.cpp',
				'src/ports/SkTLS_pthread.cpp',
				'src/ports/SkTLS_win.cpp',
				#'src/ports/SkXMLParser_empty.cpp',
				#'src/ports/SkXMLParser_expat.cpp',
				#'src/ports/SkXMLParser_tinyxml.cpp',
				#'src/ports/SkXMLPullParser_expat.cpp',
				
				'src/utils/SkOSFile.cpp',
			],
			
			# Exclude all non-generic optimisations by default
			'sources/':
			[
				['exclude', 'opts/.+\\.(cpp|S)$'],
				['include', 'opts/.+_none\\.cpp$'],
			],
			
			'conditions':
			[
				[
					'OS == "win"',
					{
						'sources/':
						[
							# We don't support DirectWrite (requires Vista and up)
							['exclude', '_win_dw\\.cpp$'],
							
							# Disable POSIX features
							['exclude', '(pthread|Unix|ashmem)\\.cpp$'],
						],
						
						# Things that don't compile
						'sources!':
						[
							'src/image/SkImage_Gpu.cpp',
							'src/image/SkSurface_Gpu.cpp',
							'src/core/SkAdvancedTypefaceMetrics.cpp',
						],
					},
				],
				[
					'OS != "win"',
					{
						'sources/':
						[
							['exclude', '_win(_dw)?.cpp$'],
						],
					},
				],
				[
					'OS != "android"',
					{
						'sources!':
						[
							'src/ports/SkFontHost_fontconfig.cpp',
						]
					},
				],
				[
					# All Intel Macs support SSE2 or above
					'OS == "mac"',
					{
						'sources/':
						[
							['include', 'opts/Sk.+_SSE2\\.cpp$'],
							['include', 'opts/.+_mac\\.cpp$'],
						],
					},
				],
			],
			
			'direct_dependent_settings':
			{
				'include_dirs':
				[
					'include/config',
					'include/core',
					'include/device',
					'include/effects',
					'include/gpu',
					'include/images',
					'include/pathops',
					'include/pdf',
					'include/pipe',
					'include/ports',
					'include/svg',
					'include/text',
					'include/utils',
				],
			},
		},
	],
}

{
	'includes':
	[
		'../../common.gypi',
	],
	
	'targets':
	[
		{
			'target_name': 'libcef_library_wrapper',
			'type': 'static_library',
			
			# Windows and OSX only
			'conditions':
			[
				[
					'OS != "mac" and OS != "win"',
					{
						'type': 'none',
					},
				],
				[
					'OS == "win"',
					{
						'defines':
						[
							'NOMINMAX',
						],
					},
				],
			],
			
			'include_dirs':
			[
				'.',
			],
			
			'defines':
			[
				# A whole pile of configuration options...
				'ANGLE_DX11',
				'CHROMIUM_BUILD',
				'USE_LIBJPEG_TURBO=1',
				'ENABLE_ONE_CLICK_SIGNIN',
				'ENABLE_REMOTING=1',
				'ENABLE_WEBRTC=1',
				'ENABLE_PEPPER_CDMS',
				'ENABLE_CONFIGURATION_POLICY',
				'ENABLE_INPUT_SPEECH',
				'ENABLE_NOTIFICATIONS',
				'ENABLE_HIDPI=1',
				'ENABLE_GPU=1',
				'ENABLE_EGLIMAGE=1',
				'ENABLE_TASK_MANAGER=1',
				'ENABLE_EXTENSIONS=1',
				'ENABLE_PLUGIN_INSTALLATION=1',
				'ENABLE_PLUGINS=1',
				'ENABLE_SESSION_SERVICE=1',
				'ENABLE_THEMES=1',
				'ENABLE_AUTOFILL_DIALOG=1',
				'ENABLE_BACKGROUND=1',
				'ENABLE_AUTOMATION=1',
				'ENABLE_GOOGLE_NOW=1',
				'CLD_VERSION=1',
				'ENABLE_FULL_PRINTING=1',
				'ENABLE_PRINTING=1',
				'ENABLE_SPELLCHECK=1',
				'ENABLE_CAPTIVE_PORTAL_DETECTION=1',
				'ENABLE_APP_LIST=1',
				'ENABLE_SETTINGS_APP=1',
				'ENABLE_MANAGED_USERS=1',
				'USING_CEF_SHARED',
				'__STDC_CONSTANT_MACROS',
				'__STDC_FORMAT_MACROS',
				'DYNAMIC_ANNOTATIONS_ENABLED=1',
				'WTF_USE_DYNAMIC_ANNOTATIONS=1',
			],
			
			'sources':
			[
				'libcef_dll/transfer_util.h',
				'libcef_dll/cpptoc/app_cpptoc.h',
				'libcef_dll/cpptoc/base_cpptoc.h',
				'libcef_dll/cpptoc/browser_process_handler_cpptoc.h',
				'libcef_dll/cpptoc/client_cpptoc.h',
				'libcef_dll/cpptoc/completion_callback_cpptoc.h',
				'libcef_dll/cpptoc/context_menu_handler_cpptoc.h',
				'libcef_dll/cpptoc/cookie_visitor_cpptoc.h',
				'libcef_dll/cpptoc/cpptoc.h',
				'libcef_dll/cpptoc/dialog_handler_cpptoc.h',
				'libcef_dll/cpptoc/display_handler_cpptoc.h',
				'libcef_dll/cpptoc/domevent_listener_cpptoc.h',
				'libcef_dll/cpptoc/domvisitor_cpptoc.h',
				'libcef_dll/cpptoc/download_handler_cpptoc.h',
				'libcef_dll/cpptoc/drag_handler_cpptoc.h',
				'libcef_dll/cpptoc/end_tracing_callback_cpptoc.h',
				'libcef_dll/cpptoc/focus_handler_cpptoc.h',
				'libcef_dll/cpptoc/geolocation_handler_cpptoc.h',
				'libcef_dll/cpptoc/get_geolocation_callback_cpptoc.h',
				'libcef_dll/cpptoc/jsdialog_handler_cpptoc.h',
				'libcef_dll/cpptoc/keyboard_handler_cpptoc.h',
				'libcef_dll/cpptoc/life_span_handler_cpptoc.h',
				'libcef_dll/cpptoc/load_handler_cpptoc.h',
				'libcef_dll/cpptoc/print_handler_cpptoc.h',
				'libcef_dll/cpptoc/read_handler_cpptoc.h',
				'libcef_dll/cpptoc/render_handler_cpptoc.h',
				'libcef_dll/cpptoc/render_process_handler_cpptoc.h',
				'libcef_dll/cpptoc/request_context_handler_cpptoc.h',
				'libcef_dll/cpptoc/request_handler_cpptoc.h',
				'libcef_dll/cpptoc/resource_bundle_handler_cpptoc.h',
				'libcef_dll/cpptoc/resource_handler_cpptoc.h',
				'libcef_dll/cpptoc/run_file_dialog_callback_cpptoc.h',
				'libcef_dll/cpptoc/scheme_handler_factory_cpptoc.h',
				'libcef_dll/cpptoc/string_visitor_cpptoc.h',
				'libcef_dll/cpptoc/task_cpptoc.h',
				'libcef_dll/cpptoc/urlrequest_client_cpptoc.h',
				'libcef_dll/cpptoc/v8accessor_cpptoc.h',
				'libcef_dll/cpptoc/v8handler_cpptoc.h',
				'libcef_dll/cpptoc/web_plugin_info_visitor_cpptoc.h',
				'libcef_dll/cpptoc/web_plugin_unstable_callback_cpptoc.h',
				'libcef_dll/cpptoc/write_handler_cpptoc.h',
				'libcef_dll/ctocpp/allow_certificate_error_callback_ctocpp.h',
				'libcef_dll/ctocpp/auth_callback_ctocpp.h',
				'libcef_dll/ctocpp/base_ctocpp.h',
				'libcef_dll/ctocpp/before_download_callback_ctocpp.h',
				'libcef_dll/ctocpp/binary_value_ctocpp.h',
				'libcef_dll/ctocpp/browser_ctocpp.h',
				'libcef_dll/ctocpp/browser_host_ctocpp.h',
				'libcef_dll/ctocpp/callback_ctocpp.h',
				'libcef_dll/ctocpp/command_line_ctocpp.h',
				'libcef_dll/ctocpp/context_menu_params_ctocpp.h',
				'libcef_dll/ctocpp/cookie_manager_ctocpp.h',
				'libcef_dll/ctocpp/ctocpp.h',
				'libcef_dll/ctocpp/dictionary_value_ctocpp.h',
				'libcef_dll/ctocpp/domdocument_ctocpp.h',
				'libcef_dll/ctocpp/domevent_ctocpp.h',
				'libcef_dll/ctocpp/domnode_ctocpp.h',
				'libcef_dll/ctocpp/download_item_callback_ctocpp.h',
				'libcef_dll/ctocpp/download_item_ctocpp.h',
				'libcef_dll/ctocpp/drag_data_ctocpp.h',
				'libcef_dll/ctocpp/file_dialog_callback_ctocpp.h',
				'libcef_dll/ctocpp/frame_ctocpp.h',
				'libcef_dll/ctocpp/geolocation_callback_ctocpp.h',
				'libcef_dll/ctocpp/jsdialog_callback_ctocpp.h',
				'libcef_dll/ctocpp/list_value_ctocpp.h',
				'libcef_dll/ctocpp/menu_model_ctocpp.h',
				'libcef_dll/ctocpp/post_data_ctocpp.h',
				'libcef_dll/ctocpp/post_data_element_ctocpp.h',
				'libcef_dll/ctocpp/print_dialog_callback_ctocpp.h',
				'libcef_dll/ctocpp/print_job_callback_ctocpp.h',
				'libcef_dll/ctocpp/print_settings_ctocpp.h',
				'libcef_dll/ctocpp/process_message_ctocpp.h',
				'libcef_dll/ctocpp/quota_callback_ctocpp.h',
				'libcef_dll/ctocpp/request_context_ctocpp.h',
				'libcef_dll/ctocpp/request_ctocpp.h',
				'libcef_dll/ctocpp/response_ctocpp.h',
				'libcef_dll/ctocpp/scheme_registrar_ctocpp.h',
				'libcef_dll/ctocpp/stream_reader_ctocpp.h',
				'libcef_dll/ctocpp/stream_writer_ctocpp.h',
				'libcef_dll/ctocpp/task_runner_ctocpp.h',
				'libcef_dll/ctocpp/urlrequest_ctocpp.h',
				'libcef_dll/ctocpp/v8context_ctocpp.h',
				'libcef_dll/ctocpp/v8exception_ctocpp.h',
				'libcef_dll/ctocpp/v8stack_frame_ctocpp.h',
				'libcef_dll/ctocpp/v8stack_trace_ctocpp.h',
				'libcef_dll/ctocpp/v8value_ctocpp.h',
				'libcef_dll/ctocpp/web_plugin_info_ctocpp.h',
				'libcef_dll/ctocpp/xml_reader_ctocpp.h',
				'libcef_dll/ctocpp/zip_reader_ctocpp.h',
				'libcef_dll/wrapper/cef_browser_info_map.h',
				
				'libcef_dll/transfer_util.cpp',
				'libcef_dll/base/cef_atomicops_x86_gcc.cc',
				'libcef_dll/base/cef_bind_helpers.cc',
				'libcef_dll/base/cef_callback_helpers.cc',
				'libcef_dll/base/cef_callback_internal.cc',
				'libcef_dll/base/cef_lock.cc',
				'libcef_dll/base/cef_lock_impl.cc',
				'libcef_dll/base/cef_logging.cc',
				'libcef_dll/base/cef_ref_counted.cc',
				'libcef_dll/base/cef_string16.cc',
				'libcef_dll/base/cef_thread_checker_impl.cc',
				'libcef_dll/base/cef_thread_collision_warner.cc',
				'libcef_dll/base/cef_weak_ptr.cc',
				'libcef_dll/cpptoc/app_cpptoc.cc',
				'libcef_dll/cpptoc/browser_process_handler_cpptoc.cc',
				'libcef_dll/cpptoc/client_cpptoc.cc',
				'libcef_dll/cpptoc/completion_callback_cpptoc.cc',
				'libcef_dll/cpptoc/context_menu_handler_cpptoc.cc',
				'libcef_dll/cpptoc/cookie_visitor_cpptoc.cc',
				'libcef_dll/cpptoc/dialog_handler_cpptoc.cc',
				'libcef_dll/cpptoc/display_handler_cpptoc.cc',
				'libcef_dll/cpptoc/domevent_listener_cpptoc.cc',
				'libcef_dll/cpptoc/domvisitor_cpptoc.cc',
				'libcef_dll/cpptoc/download_handler_cpptoc.cc',
				'libcef_dll/cpptoc/drag_handler_cpptoc.cc',
				'libcef_dll/cpptoc/end_tracing_callback_cpptoc.cc',
				'libcef_dll/cpptoc/focus_handler_cpptoc.cc',
				'libcef_dll/cpptoc/geolocation_handler_cpptoc.cc',
				'libcef_dll/cpptoc/get_geolocation_callback_cpptoc.cc',
				'libcef_dll/cpptoc/jsdialog_handler_cpptoc.cc',
				'libcef_dll/cpptoc/keyboard_handler_cpptoc.cc',
				'libcef_dll/cpptoc/life_span_handler_cpptoc.cc',
				'libcef_dll/cpptoc/load_handler_cpptoc.cc',
				'libcef_dll/cpptoc/print_handler_cpptoc.cc',
				'libcef_dll/cpptoc/read_handler_cpptoc.cc',
				'libcef_dll/cpptoc/render_handler_cpptoc.cc',
				'libcef_dll/cpptoc/render_process_handler_cpptoc.cc',
				'libcef_dll/cpptoc/request_context_handler_cpptoc.cc',
				'libcef_dll/cpptoc/request_handler_cpptoc.cc',
				'libcef_dll/cpptoc/resource_bundle_handler_cpptoc.cc',
				'libcef_dll/cpptoc/resource_handler_cpptoc.cc',
				'libcef_dll/cpptoc/run_file_dialog_callback_cpptoc.cc',
				'libcef_dll/cpptoc/scheme_handler_factory_cpptoc.cc',
				'libcef_dll/cpptoc/string_visitor_cpptoc.cc',
				'libcef_dll/cpptoc/task_cpptoc.cc',
				'libcef_dll/cpptoc/urlrequest_client_cpptoc.cc',
				'libcef_dll/cpptoc/v8accessor_cpptoc.cc',
				'libcef_dll/cpptoc/v8handler_cpptoc.cc',
				'libcef_dll/cpptoc/web_plugin_info_visitor_cpptoc.cc',
				'libcef_dll/cpptoc/web_plugin_unstable_callback_cpptoc.cc',
				'libcef_dll/cpptoc/write_handler_cpptoc.cc',
				'libcef_dll/ctocpp/allow_certificate_error_callback_ctocpp.cc',
				'libcef_dll/ctocpp/auth_callback_ctocpp.cc',
				'libcef_dll/ctocpp/before_download_callback_ctocpp.cc',
				'libcef_dll/ctocpp/binary_value_ctocpp.cc',
				'libcef_dll/ctocpp/browser_ctocpp.cc',
				'libcef_dll/ctocpp/browser_host_ctocpp.cc',
				'libcef_dll/ctocpp/callback_ctocpp.cc',
				'libcef_dll/ctocpp/command_line_ctocpp.cc',
				'libcef_dll/ctocpp/context_menu_params_ctocpp.cc',
				'libcef_dll/ctocpp/cookie_manager_ctocpp.cc',
				'libcef_dll/ctocpp/dictionary_value_ctocpp.cc',
				'libcef_dll/ctocpp/domdocument_ctocpp.cc',
				'libcef_dll/ctocpp/domevent_ctocpp.cc',
				'libcef_dll/ctocpp/domnode_ctocpp.cc',
				'libcef_dll/ctocpp/download_item_callback_ctocpp.cc',
				'libcef_dll/ctocpp/download_item_ctocpp.cc',
				'libcef_dll/ctocpp/drag_data_ctocpp.cc',
				'libcef_dll/ctocpp/file_dialog_callback_ctocpp.cc',
				'libcef_dll/ctocpp/frame_ctocpp.cc',
				'libcef_dll/ctocpp/geolocation_callback_ctocpp.cc',
				'libcef_dll/ctocpp/jsdialog_callback_ctocpp.cc',
				'libcef_dll/ctocpp/list_value_ctocpp.cc',
				'libcef_dll/ctocpp/menu_model_ctocpp.cc',
				'libcef_dll/ctocpp/post_data_ctocpp.cc',
				'libcef_dll/ctocpp/post_data_element_ctocpp.cc',
				'libcef_dll/ctocpp/print_dialog_callback_ctocpp.cc',
				'libcef_dll/ctocpp/print_job_callback_ctocpp.cc',
				'libcef_dll/ctocpp/print_settings_ctocpp.cc',
				'libcef_dll/ctocpp/process_message_ctocpp.cc',
				'libcef_dll/ctocpp/quota_callback_ctocpp.cc',
				'libcef_dll/ctocpp/request_context_ctocpp.cc',
				'libcef_dll/ctocpp/request_ctocpp.cc',
				'libcef_dll/ctocpp/response_ctocpp.cc',
				'libcef_dll/ctocpp/scheme_registrar_ctocpp.cc',
				'libcef_dll/ctocpp/stream_reader_ctocpp.cc',
				'libcef_dll/ctocpp/stream_writer_ctocpp.cc',
				'libcef_dll/ctocpp/task_runner_ctocpp.cc',
				'libcef_dll/ctocpp/urlrequest_ctocpp.cc',
				'libcef_dll/ctocpp/v8context_ctocpp.cc',
				'libcef_dll/ctocpp/v8exception_ctocpp.cc',
				'libcef_dll/ctocpp/v8stack_frame_ctocpp.cc',
				'libcef_dll/ctocpp/v8stack_trace_ctocpp.cc',
				'libcef_dll/ctocpp/v8value_ctocpp.cc',
				'libcef_dll/ctocpp/web_plugin_info_ctocpp.cc',
				'libcef_dll/ctocpp/xml_reader_ctocpp.cc',
				'libcef_dll/ctocpp/zip_reader_ctocpp.cc',
				'libcef_dll/wrapper/cef_byte_read_handler.cc',
				'libcef_dll/wrapper/cef_closure_task.cc',
				'libcef_dll/wrapper/cef_message_router.cc',
				'libcef_dll/wrapper/cef_stream_resource_handler.cc',
				'libcef_dll/wrapper/cef_xml_object.cc',
				'libcef_dll/wrapper/cef_zip_archive.cc',
				'libcef_dll/wrapper/libcef_dll_wrapper.cc',
				'libcef_dll/wrapper/libcef_dll_wrapper2.cc',
			],
			
			'direct_dependent_settings':
			{
				'include_dirs':
				[
					'.',
				],
			},
			
			'msvs_settings':
			{
				'VCCLCompilerTool':
				{
					'ExceptionHandling': '1',
				},
			},
		},
		
		{
			'target_name': 'libcef_stubs',
			'type': 'static_library',
			
			# Windows and OSX only
			'conditions':
			[
				[
					'OS != "mac" and OS != "win"',
					{
						'type': 'none',
					},
				],
			],
			
			'sources':
			[
				'<(INTERMEDIATE_DIR)/src/libcefstubs.cpp',
			],
			
			'actions':
			[
				{
					'action_name': 'generate_libcef_stubs',
					'inputs':
					[
						'../../tools/weak_stub_maker.lc',
						'libcef.stubs',
					],
					'outputs':
					[
						'<(INTERMEDIATE_DIR)/src/libcefstubs.cpp',
					],
					
					'action':
					[
						'<(revolution_path)',
						'../../tools/weak_stub_maker.lc',
						'libcef.stubs',
						'<@(_outputs)',
					],
				},
			],
		},
	],
}

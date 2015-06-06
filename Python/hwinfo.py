print('###CPU###')
try:
    from cpuinfo import cpuinfo
    cpuinfo_available = True
except ImportError:
    print('py-cpuinfo required')
    print('Install with: pip install py-cpuinfo')
    cpuinfo_available = False

if cpuinfo_available:
    cpu_info = cpuinfo.get_cpu_info()

    print('Vendor ID: {0}'.format(cpu_info['vendor_id']))
    print('Brand: {0}'.format(cpu_info['brand']))
    print('Hz Advertised: {0}'.format(cpu_info['hz_advertised']))
    print('Hz Actual: {0}'.format(cpu_info['hz_actual']))
    print('Hz Advertised Raw: {0}'.format(cpu_info['hz_advertised_raw']))
    print('Hz Actual Raw: {0}'.format(cpu_info['hz_actual_raw']))
    print('Arch: {0}'.format(cpu_info['arch']))
    print('Bits: {0}'.format(cpu_info['bits']))
    print('Count: {0}'.format(cpu_info['count']))

    print('Raw Arch String: {0}'.format(cpu_info['raw_arch_string']))

    print('L2 Cache Size: {0}'.format(cpu_info['l2_cache_size']))
    print('L2 Cache Line Size: {0}'.format(cpu_info['l2_cache_line_size']))
    print('L2 Cache Associativity: {0}'.format(cpu_info['l2_cache_associativity']))

    print('Stepping: {0}'.format(cpu_info['stepping']))
    print('Model: {0}'.format(cpu_info['model']))
    print('Family: {0}'.format(cpu_info['family']))
    print('Processor Type: {0}'.format(cpu_info['processor_type']))
    print('Extended Model: {0}'.format(cpu_info['extended_model']))
    print('Extended Family: {0}'.format(cpu_info['extended_family']))
    print('Flags: {0}'.format(', '.join(cpu_info['flags'])))

print('')
print('###Display###')
try:
    import pygame
    from pygame.locals import *
    pygame_available = True
except ImportError:
    print('pygame required')
    pygame_available = False

if pygame_available:
    pygame.init()
    display_info = pygame.display.Info()
    print('HW accelerated: {0}'.format(display_info.hw))
    print('Windowed mode supported: {0}'.format(display_info.wm))
    print('Video memory: {0} MB'.format(display_info.video_mem))
    print('Bits per pixel {0}'.format(display_info.bitsize))
    print('Bytes per pixel: {0}'.format(display_info.bytesize))
    print('Pixel masks: {0}'.format(display_info.masks))
    print('Pixel shifts: {0}'.format(display_info.shifts))
    print('Pixel losses: {0}'.format(display_info.losses))
    print('HW blitting: {0}'.format(display_info.blit_hw))
    print('HW colorkey blitting: {0}'.format(display_info.blit_hw_CC))
    print('HW alpha blitting: {0}'.format(display_info.blit_hw_A))
    print('SW blitting: {0}'.format(display_info.blit_sw))
    print('SW colorkey blitting: {0}'.format(display_info.blit_sw_CC))
    print('SW alpha blitting: {0}'.format(display_info.blit_sw_A))
    print('Current size: {0}x{1}'.format(display_info.current_w,display_info.current_h))

    print('Available modes: {0}'.format(', '.join('{0}x{1}'.format(k[1][0], k[1][1]) for k in enumerate(pygame.display.list_modes()))))

print('')
print('###OpenGL###')
try:
    from OpenGL.GL import *
    opengl_available = True
except ImportError:
    print('PyOpenGL required')
    print('Install with: pip install PyOpenGL')
    opengl_available = False

if not pygame_available:
    print('pygame required')

if pygame_available and opengl_available:
    pygame.display.set_mode((640,480), OPENGL)
    print('Version: {0}'.format(glGetString(GL_VERSION).decode("utf-8")))
    print('Vendor: {0}'.format(glGetString(GL_VENDOR).decode("utf-8")))
    print('Renderer: {0}'.format(glGetString(GL_RENDERER).decode("utf-8")))
    print('Extensions: {0}'.format(glGetString(GL_EXTENSIONS).decode("utf-8")))

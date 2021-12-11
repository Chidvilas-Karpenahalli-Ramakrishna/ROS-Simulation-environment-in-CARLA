import glob
import os
import sys
import random
import time


try:
    # --------------
    # Check python version
    # --------------
    sys.path.append(glob.glob(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) +
                              '/carla/dist/carla-*%d.%d-%s.egg' % (sys.version_info.major,
                                                                   sys.version_info.minor,
                                                                   'win-amd64' if os.name == 'nt'
                                                                   else 'linux-x86_64'))[0])
except IndexError:
    pass

import carla

actor_list = []

try:
    # --------------
    # Part A: Connecting to the server
    # --------------
    client = carla.Client("localhost", 2000)
    client.set_timeout(2.0)
    world = client.get_world()
    blueprint_library = world.get_blueprint_library()
    

    # --------------
    # Let's make it rain:
    # --------------
    weather = world.get_weather()
    weather.precipitation = 50
    world.set_weather(weather)
    

    # EGO-vehicle:
    # --------------
    bp_ego = blueprint_library.filter("model3")[0]
    # Let's set it as the EGO
    bp_ego.set_attribute('role_name','ego')
    spawn_point = random.choice(world.get_map().get_spawn_points())
    vehicle = world.spawn_actor(bp_ego, spawn_point)
    actor_list.append(vehicle)
    vehicle.set_autopilot(True)
    

    # --------------
    # Set the spectator:
    # --------------
    spectator = world.get_spectator()
    world_snapshot = world.wait_for_tick() 
    spectator.set_transform(vehicle.get_transform())
    

    # --------------
    # Attach an RGB-A camera:
    # --------------
    cam_bp = None
    cam_bp = world.get_blueprint_library().find('sensor.camera.rgb')
    cam_bp.set_attribute("image_size_x",str(1920))
    cam_bp.set_attribute("image_size_y",str(1080))
    cam_bp.set_attribute("fov",str(105))
    cam_location = carla.Location(2,0,1)
    cam_rotation = carla.Rotation(0,0,0)
    cam_transform = carla.Transform(cam_location,cam_rotation)
    ego_cam = world.spawn_actor(cam_bp,cam_transform,attach_to=vehicle, attachment_type=carla.AttachmentType.Rigid)
    ego_cam.listen(lambda image: image.save_to_disk('shk/output/%.6d.jpg' % image.frame))


    # --------------
    # Add a new semantic segmentation camera to my ego
    # --------------
    sem_cam = None
    sem_bp = world.get_blueprint_library().find('sensor.camera.semantic_segmentation')
    sem_bp.set_attribute("image_size_x",str(1920))
    sem_bp.set_attribute("image_size_y",str(1080))
    sem_bp.set_attribute("fov",str(105))
    sem_location = carla.Location(2,0,1)
    sem_rotation = carla.Rotation(0,0,0)
    sem_transform = carla.Transform(sem_location,sem_rotation)
    sem_cam = world.spawn_actor(sem_bp,sem_transform,attach_to=vehicle, attachment_type=carla.AttachmentType.Rigid)
    # This time, a color converter is applied to the image, to get the semantic segmentation view
    sem_cam.listen(lambda image: image.save_to_disk('shk/new_sem_output/%.6d.jpg' % image.frame,carla.ColorConverter.CityScapesPalette))


    # --------------
    # Add a new LIDAR sensor to my ego
    # --------------
    lidar_cam = None
    lidar_bp = world.get_blueprint_library().find('sensor.lidar.ray_cast')
    lidar_bp.set_attribute('channels',str(32))
    lidar_bp.set_attribute('points_per_second',str(90000))
    lidar_bp.set_attribute('rotation_frequency',str(40))
    lidar_bp.set_attribute('range',str(20))
    lidar_location = carla.Location(0,0,2)
    lidar_rotation = carla.Rotation(0,0,0)
    lidar_transform = carla.Transform(lidar_location,lidar_rotation)
    lidar_sen = world.spawn_actor(lidar_bp,lidar_transform,attach_to=vehicle)
    lidar_sen.listen(lambda point_cloud: point_cloud.save_to_disk('shk/new_lidar_output/%.6d.ply' % point_cloud.frame))


    # --------------
    # Get bird's eye view:
    # --------------
    bev_bp = None
    bev_bp = world.get_blueprint_library().find('sensor.camera.rgb')
    bev_bp.set_attribute("image_size_x",str(1920))
    bev_bp.set_attribute("image_size_y",str(1080))
    bev_bp.set_attribute("fov",str(105))
    bev_location = carla.Location(0,0,50)
    bev_rotation = carla.Rotation(270,0,0)
    bev_transform = carla.Transform(bev_location,bev_rotation)
    ego_bev = world.spawn_actor(bev_bp,bev_transform,attach_to=vehicle, attachment_type=carla.AttachmentType.Rigid)
    ego_bev.listen(lambda image: image.save_to_disk('shk/bev/%.6d.jpg' % image.frame))

    time.sleep(1000)

finally:
    for actor in actor_list:
        actor.destroy()
    print("Cleaned up the simulation environment.")

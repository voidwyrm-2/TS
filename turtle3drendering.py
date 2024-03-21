# This is the Demo/example script on how to use Turtle3D
# When running this demo, the controls are as follows:
# - Hold W/A/S/D for Forwards/Backwards/Left/Right movement respectfully
# - Hold arrow keys for rotating in each direction.
# This script should showcase the basic abilities of Turtle3D.

import Turtle3D
import time

def create_material():
    """Create a shiny gold material for the 3D objects."""
    return Turtle3D.Material(
        name="Shiny Gold Metal",
        ambient_color=(255, 255, 255),
        diffuse_color=(255, 255, 255),
        specular_color=(255, 255, 255),
        specular_coefficient=100
    )

def setup_scene():
    """Set up the scene with lights and a camera."""
    scene = Turtle3D.Scene("Test Scene", ambient_light=(25, 25, 25))

    # Add lights to the scene
    light_1 = Turtle3D.Light('Blue', position=[0, 0, -20], color=(64, 64, 255), intensity=0.7)
    light_2 = Turtle3D.Light('Red', position=[75, 0, -20], color=(255, 64, 64), intensity=0.7)
    scene.add_light(light_1)
    scene.add_light(light_2)

    # Set up the camera
    camera = Turtle3D.Camera("Main Camera", x_clamp=[-89, 89], fov=90, position=[37.5,0,-100])
    scene.set_active_camera(camera)

    return scene, camera

def load_objects(scene, material, file: str):
    """Load the 3D objects and add them to the scene."""
    # Load an OBJ file
    vertices, faces = Turtle3D.load_obj_file(file)

    # Create multiple objects with the same model but different positions
    objects = [
        Turtle3D.Object(f"object_{i}", vertices, faces, material=material, scale=0.075, position=[i*25, 0, 0])
        for i in range(4)
    ]
    
    # Add objects to the scene
    for obj in objects:
        scene.add_object(obj)

def main(file: str):
    """Main function to set up and run the demo."""
    # Initialize scene and material
    material = create_material()
    scene, camera = setup_scene()

    # Load objects into the scene
    load_objects(scene, material, file)

    # Toggle full screen for the global window
    Turtle3D.global_window.toggle_full_screen()

    # Start the main loop
    while True:

        # Rotate every object in the scene
        for object in scene._object_memory:
            object.rotate(1,1,1)

        # Render the scene
        try:
            scene.render_scene()
        except:
            break
        
        # Sleep to achieve the desired frame rate (approximately 60 FPS)
        time.sleep(1/60)
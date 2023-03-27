cd VILP/image_generation
/usr/bin/blender-2.78c-linux-glibc219-x86_64/blender --background --python render_vilp.py -- --dataset member --num_images 50
/usr/bin/blender-2.78c-linux-glibc219-x86_64/blender --background --python render_vilp.py -- --dataset delete --num_images 50
/usr/bin/blender-2.78c-linux-glibc219-x86_64/blender --background --python render_vilp.py -- --dataset append --num_images 50
/usr/bin/blender-2.78c-linux-glibc219-x86_64/blender --background --python render_vilp.py -- --dataset sort --num_images 50

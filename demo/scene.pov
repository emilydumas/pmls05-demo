// POV-Ray scene file for PML(S_{0,5}) demo
//
// From the PML Visualization Project (http://dumas.io/PML/)
// by David Dumas and Francois Gueritaud

#include "colors.inc"
#include "shapes.inc"
#include "textures.inc"

global_settings {
	assumed_gamma 1.0
	max_trace_level 30
	ambient_light rgb<0.5,0.5,0.5>
}

camera {
        location <8, 1,1>
	sky (image_width/image_height)*<0 0 1>
	right 0.8*(image_width/image_height)*<0 1 0>
	up 0.8*<0 0 1>
        look_at <0,0,0>
}
 
light_source {
        <0, 0, 10>
        color rgb <1.1,1.1,1.1>
}

light_source {
        <50,10,-1>
        color rgb 0.5*<1,1,1>
	shadowless
}

sky_sphere {
  pigment { rgb<0.83,0.8,0.7> }
}

#declare DATAFILE="spheres.inc";

union {
#include DATAFILE
  material {
    texture {

     pigment { rgb<0.0,0.05,0.400> }
     finish {
        ambient 0.0
        specular 0.70
        roughness 0.05
     }
    }
  }
  no_shadow

  // This rotation is only used for rendering an animation
  // (defaults to zero rotation when rendering a single image)
  rotate 360*clock*z
}

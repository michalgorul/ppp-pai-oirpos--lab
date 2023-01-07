window.onload = function () {
    element_box= document.querySelector('#box');
    element_sphere = document.querySelector('#sphere');
    element_cylinder = document.querySelector('#cylinder');
    rig = document.querySelector('#rig')
    camera = document.querySelector('#camera')
};
var t = 0.0
setInterval(function() {
    t += 0.005
}, 10)

animate_box = function () {
    element_box.components.rotation.data.x += 0.5
    element_box.components.rotation.update()
    // element_box.object3D.rotateX(0.0001)
}
setInterval(animate_box, 10)

animate_sphere = function() {
    var sin_t = Math.sin(t)
    element_sphere.object3D.scale.set(sin_t, sin_t, sin_t)
}
setInterval(animate_sphere, 10)


animate_cylinder = function() {
    var r = Math.sin(t)
    var g = Math.sin(2 * t)
    var b = Math.cos(t)
    const color = new THREE.Color(r, g, b)
    element_cylinder.components.material.material.color = color
}
setInterval(animate_cylinder,10)


animate_rig = function() {
    var rig_pos = new THREE.Vector3(0.0, 0.0, 0.0)
    rig_pos.x = Math.sin(t) * 10
    rig_pos.z = Math.cos(t) * 10
    rig.object3D.position.x = rig_pos.x
    rig.object3D.position.z = rig_pos.z
    var rad = Math.atan2(rig_pos.x, rig_pos.z)
    rig.object3D.rotation.y = rad
}
setInterval(animate_rig, 10)


AFRAME.registerComponent('box', {
    schema: {
      width: {type: 'number', default: 1},
      height: {type: 'number', default: 1},
      depth: {type: 'number', default: 1},
      color: {type: 'color', default: '#AAA'}
    },

    /**
     * Initial creation and setting of the mesh.
     */
    init: function () {
      var data = this.data;
      var el = this.el;

      // Create geometry.
      this.geometry = new THREE.BoxBufferGeometry(data.width, data.height, data.depth);

      // Create material.
      this.material = new THREE.MeshStandardMaterial({color: data.color});

      // Create mesh.
      this.mesh = new THREE.Mesh(this.geometry, this.material);

      // Set mesh on entity.
      el.setObject3D('mesh', this.mesh);
    },
    tick: function (time, timeDelta) {
        this.el.object3D.rotation.x += timeDelta / 100
        this.el.object3D.rotation.y += timeDelta / 300.0
    }
  });

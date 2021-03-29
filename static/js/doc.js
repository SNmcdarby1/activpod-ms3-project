 document.addEventListener('DOMContentLoaded', function() {
     var elems = document.querySelectorAll('.tap-target');
     var instances = M.TapTarget.init(elems, options);
 });

 // Or with jQuery

 $(document).ready(function() {
     $('.tap-target').tapTarget();
 });

 //content
 var instance = M.TapTarget.getInstance(elem);
 instance.next();
 instance.next(3); // Move next n times.

 instance.close();

 instance.destroy();
 // media
 var instance = M.Materialbox.getInstance(elem);
 document.addEventListener('DOMContentLoaded', function() {
     var elems = document.querySelectorAll('.materialboxed');
     var instances = M.Materialbox.init(elems, options);
 });

 // Or with jQuery

 $(document).ready(function() {
     $('.materialboxed').materialbox();
 });
<template>
  <video ref="video" width="100%" height="640" controls></video>
</template>

<script>
import Hls from 'hls.js';

export default {
  mounted() {
    let hls = new Hls();
    let stream = "http://38.242.237.26:2082/live/mostafa/said/13.m3u8";
    let video = this.$refs["video"];
    hls.loadSource(stream);
    hls.attachMedia(video);
    hls.on(Hls.Events.MANIFEST_PARSED, function () {
      video.play();
    });
  },
};
</script>
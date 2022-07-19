<doc>
Video components
</doc>
<template>
<video id="video" style="width: 100%;height: 100%;" class="video-js vjs-default-skin" preload="auto">
<!-- <source :src="url" type="application/x-mpegURL"> -->
<!-- <source src="https://cdn.theguardian.tv/webM/2015/07/20/150716YesMen_synd_768k_vp8.webm" type="application/x-mpegURL"> -->
<source src="http://38.242.237.26:2082/live/mostafa/said/13.m3u8" type="application/x-mpegURL">
<!-- <source src="https://bitdash-a.akamaihd.net/content/sintel/hls/playlist.m3u8" type="application/x-mpegURL"> -->
</video>
</template>
<script>
import videojs from 'video.js'
import 'videojs-contrib-hls'
import "@videojs/http-streaming"
export default {
props : ['url'],
data() {

return {

player: null,
}
},
mounted() {

this.init()
},
methods: {

init() {

// Player initialization 
this.$nextTick(() => {

this.player = videojs('video' , {

bigPlayButton: false,
textTrackDisplay: false,
posterImage: true,
errorDisplay: false,
controlBar: false,
muted: true // Mute mode 、、 Solve the problem of first page loading and playing .
}, function () {

this.play() // Auto play 
})
})
}
},
// Leave the page and destroy the video player 
beforeDestroy() {

if (this.player != null) {

this.player.dispose() // dispose() Will delete Dom Elements 
}
}
}
</script>
<style scoped>
</style>
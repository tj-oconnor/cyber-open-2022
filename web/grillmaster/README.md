# Grillmaster

A CTFd compatible docker image for a web challenge. Scenario: A burger shop is accepting entries for its new menu. Users can select the ingredients they would like to see on a recipe and submit it. Then, a state-of-the-art AI called "The Grillmaster" will review each one and determine if it sounds delicious enough. The best recipe gets a special prize!

## Setup

Run the included build-docker.sh script to build and deploy the container in docker.

## Solution

See solution video for full details. The Grillmaster bot is wide open to cross-site scripting attacks, so you need to direct him to approve a submission. This can be achieved by simply placing something like the following script in the comments box:

```
<script> window.location+="/approve"; </script>
```


---
date: 2019-04-27 15:25:35+00:00
reply_to:
  label: '''Assign Multiple Keys for jumping?'' on /r/Unity2D'
  name: ''
  type: reddit
  url: https://reddit.com/r/Unity2D/comments/bhzosq/assign_multiple_keys_for_jumping/
source: reddit
syndicated:
- type: reddit
  url: https://www.reddit.com/r/Unity2D/comments/bhzosq/assign_multiple_keys_for_jumping/elwzgr2/
tags:
- Unity2D
---

Maybe all three keys are firing the update separately? Try setting isGround to false after \`myRigidbody.AddForce(new Vector2(0, jumpForce), ForceMode2D.Impulse);\`
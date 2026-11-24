# Hospital fall monitor prompt for Claude Code

A visual patient-state monitor: works with any camera you name, watches each patient's state (standing, walking, sitting, lying on the floor), knows who is who from the wristband code even in bad light, and fires the nurse call + EHR alert seconds after a fall. Paste into Claude Code. Runs fully local; the demo uses a mock nurse call board.

No Claude yet? [Get Claude here](https://claude.ai/referral/IL0FPScZCw).

```
You have a Python environment. Goal: build a visual patient-state monitoring system that works with any camera model I name, knows which patient it is watching, tracks their position and state (standing, walking, sitting, lying on the floor), and alerts that patient's nurse the moment they fall and stay down.

Setup
- Install ultralytics + opencv-python. Use YOLOv8n-pose as the person model (it only feeds the body angle, nothing is drawn as a skeleton). Everything runs locally on CPU.
- Camera: I will tell you the camera model. Look up its stream (RTSP/ONVIF), resolution and night mode, and put it in cameras.yaml. Webcam 0 or `--video path.mp4` also work for testing.

Per frame, for every person
1. Box around the person with their state: STANDING / WALKING / SITTING / LYING ON FLOOR. Green while monitoring, red after a fall. No skeleton overlay.
2. Torso angle: angle of the line from mid-hips to mid-shoulders against vertical (0 = standing, 90 = lying).
3. Vertical descent speed: how fast the hip center moves down, in body heights per second (smooth over 5 frames).
4. Visibility: if part of the body is hidden (a desk, a wall, a cane) or the light is bad, keep the last good estimate and mark it "IMPUTED" instead of dropping the person.

Who is who
- Keep a stable ID per person with the built-in tracker (ByteTrack).
- patients.json maps each patient to an MRN (patient ID), name, room, bed and assigned nurse.
- Identify the patient by the code on their wristband (barcode/QR, like hospitals already print). Read it whenever it is visible and keep the ID on the track after that, so the patient stays known in bad light, at a distance or with their back to the camera. No face recognition.
- If the link is unsure, say "UNKNOWN PATIENT" in the alert instead of guessing.

Fall logic
- FALL = descent speed above a threshold AND torso angle > 60 deg within 1 second.
- Then a 4 s stillness check: if the person stays low and barely moves, show "IMPACT CONFIRMED". If they get up, cancel the alert.
- Tune both thresholds on 10 clips: 5 of me sitting down fast, bending to pick something up, lying on a sofa (must NOT fire), 5 of me doing a slow controlled fall onto a mattress (must fire). Report hits and false alarms.

Alert (US hospital style: nurse call + EHR)
- When the fall is confirmed, raise it the way a patient's call button does: a nurse call event for that patient's room and bed, priority "fall / staff emergency".
- Send it as an HL7 v2 message (ADT/ORU style, with patient ID, room, bed, time, event) and as a FHIR Observation + Flag ("fall detected") for the patient record in the EHR.
- For the demo, run a small local mock of the nurse call board + EHR inbox (one web page) that receives both and shows the alert on that patient's room tile, with a face-blurred snapshot. Real hospital wiring (Epic, Oracle Health, Rauland, Hillrom, Vocera) is a config file, not code changes.
- One alert per fall. Send a "patient up, alert cleared" update if they stand.

HUD (CCTV style)
- Top bar: system name on the left, FPS and "Tracking: N subject(s)" on the right, date + time.
- Label box above each person: patient ID + room once the wristband is read ("UNKNOWN" before that), state, "MONITORING" / "FALL DETECTED", torso angle, descent speed.
- Red bottom banner on alert: "FALL DETECTED (patient, room)" + "Verifying ground stillness (3.8s remaining)... Stand up to cancel." then "NURSE ALERTED".

Output
- patient_monitor.py, one file, runs with one command, plus cameras.yaml, patients.json and the mock nurse call page.
- demo.mp4 with the HUD burned in.
- events.csv: time, patient ID, state, torso angle, speed, alert state, seconds from fall to nurse alert.
- A short summary: thresholds you picked, hits, false alarms, FPS on my machine.

Rules
- Never upload video anywhere. No cloud AI APIs. The only thing that leaves the detector is the alert to the nurse call / EHR endpoint.
- Blur every face in saved video except mine.
- Test falls only onto a mattress. This is a demo, not a medical device, and never a replacement for staff.
```

---

Don't have Claude Code yet? [Get Claude here](https://claude.ai/referral/IL0FPScZCw).

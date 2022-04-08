from datetime import datetime, timedelta
from python_get_resolve import GetResolve

resolve = GetResolve()
project_manager = resolve.GetProjectManager()
project = project_manager.GetCurrentProject()
timeline = project.GetCurrentTimeline()

trackType = 'video'
print('GetTrackCount(trackType):', timeline.GetTrackCount(trackType))
items = timeline.GetItemListInTrack(trackType, 1)

fps = 30
offset=-108000 #frame
offset_sec = 3.03 #sec
base_time = datetime.strptime('01:00:00', '%H:%M:%S')

idx = 1
for item in items:
    name = item.GetName()
    comp = item.GetFusionCompByIndex(1).GetToolList() 
    text = comp[1].StyledText[0].replace('\r','').replace('\n','')

    duration = item.GetDuration()
    start_frame = item.GetStart()

    sec = float(start_frame+offset)/float(fps)
    duration_sec = float(duration)/float(fps)
    current_time = base_time + timedelta(seconds=sec+offset_sec)
    timecode_start = datetime.strftime(current_time, '%H:%M:%S,%f')[:-3]
    timecode_end = datetime.strftime(current_time + timedelta(seconds=duration_sec), '%H:%M:%S,%f')[:-3]
    
    print(idx)
    print(timecode_start + ' --> '+ timecode_end)
    print(text)
    print()

    idx = idx + 1
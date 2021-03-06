import subprocess as sp

user_process = ['chrome', 'vim', 'thunder', 'brave', 'opera'\
,'plank', 'AppRun', 'kdocker', 'AppImage', 'top', 'crow'\
,'anydesk', 'gimp', 'vlc', 'start','pulseaudio', 'vmware'\
,'cinnamon-set','python', 'gnome-system-mo', 'nemo'\
,'code', 'bash', 'wireshark', 'rclone', 'mega'\
]

def get_active_id():
    list_process = sp.getoutput('top -b -n 1 -u voccer -w 100').split('\n')
    list_id = []
    exclude_id = [i.strip() for i in sp.getoutput('ps -o ppid=$$').split('\n')]
    zsh_id = []
    for p in list_process[7:]:
        p = p.strip()
        name_proc, id_proc = p.split(' ')[-1], p.split(' ')[0]
        if name_proc == 'zsh':
            if id_proc not in exclude_id:
                zsh_id.append(id_proc)
            continue
        
        for up in user_process:
            if up in name_proc:
                list_id.append(id_proc)
    

    while True:
        try:
            list_id.remove('')
        except:
            break
    return list_id, zsh_id


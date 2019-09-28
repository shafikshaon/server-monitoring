import os

from django.http import JsonResponse


def get_main_memory_swap_memory(d):
    """
    Get mail memory usage
    Fet swap memory usage
    help links: https://haydenjames.io/linux-server-need-ram-upgrade-lets-check-free-top-vmstat-sar/
    https://www.geeksforgeeks.org/free-command-linux-examples/
    """
    try:
        memory = os.popen("free -tm | " + "grep 'Mem' | " + "awk '{print $2,$3,$4,$5,$6,$7}'")
        data = memory.read().strip().split()
        memory.close()

        swap_memory = os.popen("swapon -s" + "grep 'Mem' | " + "awk '{print $3,$4}'")
        swap_data = swap_memory.read().strip().split()
        swap_memory.close()

        try:
            swap_total = int(swap_data[2]) / 1024
            swap_used = int(swap_data[3]) / 1024
            swap_free = swap_total - swap_used
        except:
            swap_total = int(swap_data[2]) / 1024
            swap_used = swap_data[3]
            swap_free = swap_total - swap_used

        total = int(data[0])
        used = int(data[1])
        free = int(data[2])
        shared = int(data[3])
        buffered_cached = int(data[4])
        available = int(data[5])

        memory_dict = {
            'total': total,
            'used': used,
            'free': free,
            'shared': shared,
            'buffered_cached': buffered_cached,
            'available': available,
            'swap_total': int(swap_total),
            'swap_used': int(swap_used),
            'swap_free': int(swap_free),
        }

        data = memory_dict

    except Exception as err:
        data = str(err)

    return JsonResponse(data, safe=True)

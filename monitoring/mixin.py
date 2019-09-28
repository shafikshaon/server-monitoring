import os

from django.http import JsonResponse


def get_main_memory_swap_memory(args):
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


def get_network_information(args):
    """
    Get the Network Information
    """
    data = []
    try:
        network_interface = os.popen("ip addr | grep LOWER_UP | awk '{print $2}'")
        iface = network_interface.read().strip().replace(':', '').split('\n')
        network_interface.close()
        # del iface[0]

        for i_name in iface:
            network = os.popen("ip addr show " + i_name + "| awk '{if ($2 == \"forever\"){!$2} else {print $2}}'")
            network_data = network.read().strip().split('\n')
            network.close()
            if len(network_data) == 2:
                network_data.append('unavailable')
            if len(network_data) == 3:
                network_data.append('unavailable')
            data.append(network_data)

        networks_data = {}
        for d in data:
            if len(d) <= 4:
                ips = {
                    d[0]: {
                        'interface': d[0],
                        'mac_address': d[1],
                        'ipv4': d[2],
                        'ipv6': d[3],
                    }
                }
                networks_data.update(ips)

            if len(d) >= 5:
                ips = {
                    d[0]: {
                        'interface': d[0],
                        'mac_address': d[1],
                        'ipv4': d[2],
                        'ipv6': d[4],
                    }
                }
                networks_data.update(ips)

        data = networks_data

    except Exception as err:
        data = str(err)

    return JsonResponse(data, safe=True)

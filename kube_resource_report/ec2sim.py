from .pricing import get_node_cost

INSTANCE_SIZES = {
        't2.nano': (1, 0.5),
        't2.micro': (1, 1),
        't2.small': (1, 2),
        't2.medium': (2, 4),
        'm5.large': (2, 8),

}

RESERVED_SYSTEM_MEMORY = 200 * 1024**2

def calculate_comparable_ec2_cost(region: str, pods: list) -> int:
    cost = 0
    for pod in pods:
        instance_type = None
        for _instance_type, cpu_memory in INSTANCE_SIZES.items():
            cpu, memory = cpu_memory
            memory *= 1024**3
            memory -= RESERVED_SYSTEM_MEMORY
            if pod['requests']['cpu'] <= cpu and pod['requests']['memory'] <= memory:
                instance_type = _instance_type
                break
        print(pod, instance_type)
        cost += get_node_cost(region, instance_type, False)
    return cost


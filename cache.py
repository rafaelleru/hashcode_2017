import sys
from collections import defaultdict

f = open(sys.argv[1],'r')

#Lee primera linea
variables = f.readline()

variables = variables.split()

n__videos = int(variables[0])
n_endpoints = int(variables[1])
n_request_description = int(variables[2])
n_caches = int(variables[3])
tam_cache = int(variables[4])

#Lee segunda linea
size_videos = f.readline().split()
videos = {}
for i in range(n__videos):
    videos[i] = size_videos[i]
#print(size_videos)

endpoint = {0:{}}
for i in range(n_endpoints):
    datacenter_latency = f.readline().split()
    caches_conectadas=int(datacenter_latency[1])
    cache={}
    for j in range(caches_conectadas):
        cache_latency = f.readline().split()
        cache[int(cache_latency[0])]= int(cache_latency[1])

    endpoint[i]=cache
#print(endpoint)

peticiones = {}
endpoint_peticiones = {}
for i in range(n_request_description):
    video_endpoint_request =f.readline().split()
    numero_video = int(video_endpoint_request[0])
    numero_endpoint = int(video_endpoint_request[1])
    numero_peticiones = int(video_endpoint_request[2])
    endpoint_peticiones[numero_video]=numero_peticiones
    peticiones[numero_endpoint] = endpoint_peticiones

#print(peticiones)


servidores_cache ={}
for i in range(n_caches):
    servidores_cache[i]=0

#print(servidores_cache)

# peticiones ['ID_end': '[['IDvideo':'npeticiones']....['video_i':'npeticiones']]']
# endpoint ['ID_end': '[[cache_0:latencia_0]...[cache_i:latencia]'] array*******
# servidores_cache [['id_cache':'ocupada']...] array
# videos ['IDvideo':'peso']


def asigna_videos_a_cache():
    soluciones = []
    n_caches = []

    for idcache, ocupado in servidores_cache.items():
        for _endpoint, _peticiones in peticiones.items():

            #ordenar en relalcion a latencia con endpoint
            conectados_a_endp = endpoint[_endpoint]

            for id_video,npeticion in _peticiones.items():
                peso_video = int(videos[id_video])

                for serv_cache, ocupado in conectados_a_endp.items():
                    n_caches.append(serv_cache)
                    if ocupado+peso_video  < tam_cache:
                        soluciones.append([serv_cache, id_video])
                        
    numero_caches = (len(list(set(n_caches)))) #Numero de caches
    return soluciones,numero_caches

def mostrarSolucion(parSolucion):
    print(parSolucion[1])
    d = defaultdict(list)
    for i,j in parSolucion[0]:
        d[i].append(j)
    print(d.items())
    return d.items()

mostrarSolucion(asigna_videos_a_cache())

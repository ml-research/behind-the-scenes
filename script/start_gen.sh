docker exec -ti vilp bash -c 'nohup sh  VILP/gen_mem.sh &> output & sleep 1'
docker exec -ti vilp bash -c 'nohup sh  VILP/gen_del.sh &> output & sleep 1'
docker exec -ti vilp bash -c 'nohup sh  VILP/gen_app.sh &> output & sleep 1'
# docker exec -ti vilp bash -c 'nohup sh  VILP/gen_sort.sh &> output & sleep 1'

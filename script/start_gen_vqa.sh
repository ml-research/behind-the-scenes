docker exec -ti vilp bash -c 'nohup sh  VILP/gen_vqa_del.sh &> output_vq & sleep 1'
docker exec -ti vilp bash -c 'nohup sh  VILP/gen_vqa_app.sh &> output_vq & sleep 1'

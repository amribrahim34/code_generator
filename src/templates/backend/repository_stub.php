<?php

namespace App\Repositories;

use App\Models\{model_name};

class {class_name} implements {interface_name}
{{
    protected $model;

    public function __construct({model_name} $model)
    {{
        $this->model = $model;
    }}

    public function all()
    {{
        return $this->model->all();
    }}

    public function find($id)
    {{
        return $this->model->findOrFail($id);
    }}

    public function create(array $data)
    {{
        return $this->model->create($data);
    }}

    public function update($id, array $data)
    {{
        $record = $this->find($id);
        $record->update($data);
        return $record;
    }}

    public function delete($id)
    {{
        return $this->model->destroy($id);
    }}
}}

<?php

namespace App\Repositories;

use App\Models\{model_name};

interface {interface_name}
{{
    public function all();
    public function find($id);
    public function create(array $data);
    public function update($id, array $data);
    public function delete($id);
}}

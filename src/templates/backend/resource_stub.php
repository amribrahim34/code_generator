<?php

namespace {namespace};

use Illuminate\Http\Resources\Json\JsonResource;

class {class_name} extends JsonResource
{{
    public function toArray($request)
    {{
        return [
            {attributes}
            {relationships}
        ];
    }}
}}
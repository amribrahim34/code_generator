<?php

namespace {namespace};

use Illuminate\Foundation\Http\FormRequest;

class {class_name} extends FormRequest
{{
    public function authorize()
    {{
        return true;
    }}

    public function rules()
    {{
        return [
            {rules}
        ];
    }}

    public function messages()
    {{
        return [
            {messages}
        ];
    }}
}}
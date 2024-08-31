<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class {class_name} extends Migration
{{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {{
        Schema::create('{table_name}', function (Blueprint $table) {{
            {schema_up}
        }});
    }}

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {{
        {schema_down}
    }}
}}

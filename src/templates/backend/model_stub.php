<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
{use_soft_deletes}

class {class_name} extends Model
{{

    {table_name}
    use HasFactory;

    /**
     * The attributes that are mass assignable.
     *
     * @var array
     */
    protected $fillable = [{fillable}];

    {casts}

    

    {relationships}
}}